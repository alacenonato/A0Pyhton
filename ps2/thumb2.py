import os
import sys
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QHBoxLayout, QListView, QLabel, QFileSystemModel, 
    QTreeView, QSplitter
)
from PySide6.QtCore import Qt, QSize, QModelIndex, QDir
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtMultimedia import QMediaPlayer, QVideoSink
from PySide6.QtCore import QUrl, QEventLoop, QTimer

class ThumbnailModel(QFileSystemModel):
    """Modelo personalizado que gera thumbnails para imagens e vídeos"""
    
    def __init__(self, thumbnail_size: QSize = QSize(200, 150)):
        super().__init__()
        self.thumbnail_size = thumbnail_size
        self.video_player = None
        
        # Filtros para arquivos de imagem e vídeo
        self.setNameFilters([
            '*.png', '*.jpg', '*.jpeg', '*.bmp', '*.gif',  # Imagens
            '*.mp4', '*.avi', '*.mov', '*.mkv', '*.flv'     # Vídeos
        ])
        self.setNameFilterDisables(False)
        
    def get_thumbnail(self, index: QModelIndex) -> QPixmap:
        """Gera thumbnail para o arquivo no índice especificado"""
        if index.model().isDir(index):
            return QPixmap()
            
        file_path = self.filePath(index)
        file_ext = Path(file_path).suffix.lower()
        
        # Processar imagens
        if file_ext in ['.png', '.jpg', '.jpeg', '.bmp', '.gif']:
            pixmap = QPixmap(file_path)
            if not pixmap.isNull():
                return pixmap.scaled(
                    self.thumbnail_size,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
        
        # Processar vídeos (thumbnail do primeiro frame)
        elif file_ext in ['.mp4', '.avi', '.mov', '.mkv', '.flv']:
            thumbnail = self.extract_video_thumbnail(file_path)
            if thumbnail:
                return thumbnail.scaled(
                    self.thumbnail_size,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
        
        # Fallback: ícone padrão
        return QPixmap()
    
    def extract_video_thumbnail(self, video_path: str) -> QPixmap:
        """Extrai thumbnail de um frame do vídeo usando QMediaPlayer"""
        try:
            # Criar player e sink para capturar frames
            loop = QEventLoop()
            player = QMediaPlayer()
            video_sink = QVideoSink()
            player.setVideoSink(video_sink)
            player.setSource(QUrl.fromLocalFile(video_path))
            
            thumbnail = None
            position_set = False
            
            def handle_status(status):
                nonlocal position_set
                if status == QMediaPlayer.MediaStatus.BufferedMedia and not position_set:
                    # Posicionar no meio do vídeo (ou 1 segundo se duração não disponível)
                    duration = player.duration()
                    if duration > 0:
                        player.setPosition(duration // 2)
                    else:
                        player.setPosition(1000)  # 1 segundo
                    position_set = True
            
            def handle_frame(frame):
                nonlocal thumbnail
                # Capturar frame quando disponível
                if frame.isValid():
                    image = frame.toImage()
                    if not image.isNull():
                        thumbnail = QPixmap.fromImage(image)
                        loop.quit()
            
            # Conectar sinais
            player.mediaStatusChanged.connect(handle_status)
            video_sink.videoFrameChanged.connect(handle_frame)
            
            # Timeout para evitar loop infinito
            QTimer.singleShot(5000, loop.quit)
            
            # Iniciar playback
            player.play()
            loop.exec()
            
            # Limpeza
            player.stop()
            player.setVideoSink(None)
            
            return thumbnail
            
        except Exception as e:
            print(f"Erro ao extrair thumbnail do vídeo: {e}")
            return None
    
    def data(self, index: QModelIndex, role: int):
        """Sobrescreve método data para fornecer thumbnails"""
        if role == Qt.ItemDataRole.DecorationRole:
            # Retorna thumbnail para o item
            return self.get_thumbnail(index)
        elif role == Qt.ItemDataRole.DisplayRole:
            # Mostra apenas o nome do arquivo
            return self.fileName(index)
        elif role == Qt.ItemDataRole.ToolTipRole:
            # Mostra caminho completo no tooltip
            return self.filePath(index)
        else:
            return super().data(index, role)


class ThumbnailApp(QMainWindow):
    """Aplicação principal com navegador de thumbnails"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Navegador de Mídia - Thumbnails")
        self.setGeometry(100, 100, 1000, 700)
        
        # Configurar modelo e views
        self.setup_ui()
        
        # Iniciar na pasta home do usuário
        home_dir = str(Path.home())
        self.set_current_directory(home_dir)
    
    def setup_ui(self):
        """Configura a interface do usuário"""
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QHBoxLayout(central_widget)
        
        # Splitter para redimensionar painéis
        splitter = QSplitter(Qt.Orientation.Horizontal)
        main_layout.addWidget(splitter)
        
        # Painel esquerdo: TreeView para navegação de pastas
        self.folder_view = QTreeView()
        self.folder_model = QFileSystemModel()
        self.folder_model.setRootPath(QDir.rootPath())
        self.folder_model.setFilter(QDir.Filter.AllDirs | QDir.Filter.NoDotAndDotDot)
        
        self.folder_view.setModel(self.folder_model)
        self.folder_view.setHeaderHidden(True)
        self.folder_view.setIndentation(10)
        self.folder_view.setMinimumWidth(250)
        
        # Quando selecionar uma pasta, atualiza o ListView
        self.folder_view.selectionModel().selectionChanged.connect(self.on_folder_changed)
        
        # Painel direito: ListView com thumbnails
        self.thumbnail_view = QListView()
        self.thumbnail_model = ThumbnailModel()
        self.thumbnail_view.setModel(self.thumbnail_model)
        
        # Configurar visualização dos thumbnails
        self.thumbnail_view.setViewMode(QListView.ViewMode.IconMode)
        self.thumbnail_view.setIconSize(QSize(200, 150))
        self.thumbnail_view.setGridSize(QSize(220, 180))
        self.thumbnail_view.setResizeMode(QListView.ResizeMode.Adjust)
        self.thumbnail_view.setSpacing(10)
        self.thumbnail_view.setWordWrap(True)
        
        # Adicionar widgets ao splitter
        splitter.addWidget(self.folder_view)
        splitter.addWidget(self.thumbnail_view)
        
        # Configurar proporções do splitter (30% pasta, 70% thumbnails)
        splitter.setSizes([300, 700])
        
        # Barra de status
        self.status_label = QLabel("Pronto")
        self.statusBar().addWidget(self.status_label)
    
    def on_folder_changed(self, selected, deselected):
        """Callback quando uma pasta é selecionada na tree view"""
        indexes = selected.indexes()
        if indexes:
            folder_path = self.folder_model.filePath(indexes[0])
            self.set_current_directory(folder_path)
    
    def set_current_directory(self, path: str):
        """Define o diretório atual e atualiza a visualização"""
        if os.path.exists(path) and os.path.isdir(path):
            index = self.thumbnail_model.setRootPath(path)
            self.thumbnail_view.setRootIndex(index)
            self.status_label.setText(f"Exibindo: {path}")
            
            # Contar arquivos de mídia
            media_count = self.count_media_files(path)
            self.statusBar().showMessage(f"{media_count} arquivos de mídia encontrados", 3000)
    
    def count_media_files(self, path: str) -> int:
        """Conta arquivos de imagem e vídeo em uma pasta"""
        extensions = {'.png', '.jpg', '.jpeg', '.bmp', '.gif', 
                     '.mp4', '.avi', '.mov', '.mkv', '.flv'}
        
        count = 0
        try:
            for file in os.listdir(path):
                if Path(file).suffix.lower() in extensions:
                    count += 1
        except Exception:
            pass
        return count


def main():
    """Ponto de entrada da aplicação"""
    app = QApplication(sys.argv)
    
    # Configurar estilo visual
    app.setStyle('Fusion')
    
    window = ThumbnailApp()
    window.show()
    
    sys.exit(app.exec())


if __name__ == '__main__':
    main()