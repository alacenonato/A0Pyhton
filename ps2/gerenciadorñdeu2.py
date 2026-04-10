#!/usr/bin/env python3
"""
POPStarter/OPL Media Gallery - Visualizador de jogos para PC
Estilo OpenLoader, lê estrutura de HD com POPStarter e OPL
"""

import sys
import os
from pathlib import Path
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class GameInfo:
    """Informações de um jogo"""
    title: str
    game_id: str  # Ex: SLUS_012.34
    filename: str  # Nome do arquivo original
    file_ext: str  # .VCD (PS1) ou .iso (PS2)
    folder_type: str  # 'POPS' ou 'DVD' ou 'CD'
    cover_path: Optional[str]  # Caminho para capa na pasta ART
    disk_art_path: Optional[str]  # Caminho para arte do disco
    screen_path: Optional[str]  # Caminho para screenshot

class GameModel(QAbstractListModel):
    """Modelo para lista de jogos"""
    
    def __init__(self):
        super().__init__()
        self.games: List[GameInfo] = []
        self.cover_size = QSize(180, 250)
        self.thumbnail_cache = {}
        
    def rowCount(self, parent=QModelIndex()):
        return len(self.games)
    
    def add_game(self, game: GameInfo):
        """Adiciona jogo ao modelo"""
        self.beginInsertRows(QModelIndex(), len(self.games), len(self.games))
        self.games.append(game)
        self.endInsertRows()
    
    def clear(self):
        """Limpa todos os jogos"""
        self.beginResetModel()
        self.games.clear()
        self.thumbnail_cache.clear()
        self.endResetModel()
    
    def load_cover_thumbnail(self, game: GameInfo) -> QPixmap:
        """Carrega thumbnail da capa do jogo"""
        if game.game_id in self.thumbnail_cache:
            return self.thumbnail_cache[game.game_id]
        
        # Procurar capa na ordem de prioridade
        cover_paths = []
        
        if game.cover_path and os.path.exists(game.cover_path):
            cover_paths.append(game.cover_path)
        
        # Padrões OPL para capas
        art_folder = Path(game.cover_path).parent if game.cover_path else None
        if art_folder:
            cover_paths.extend([
                art_folder / f"{game.game_id}.jpg",
                art_folder / f"{game.game_id}.png",
                art_folder / f"{game.title}.jpg",
                art_folder / f"{game.title}.png"
            ])
        
        for path in cover_paths:
            if path and os.path.exists(path):
                pixmap = QPixmap(str(path))
                if not pixmap.isNull():
                    thumb = pixmap.scaled(
                        self.cover_size,
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation
                    )
                    self.thumbnail_cache[game.game_id] = thumb
                    return thumb
        
        # Capa padrão se não encontrar
        pixmap = QPixmap(self.cover_size)
        pixmap.fill(QColor(50, 50, 70))
        painter = QPainter(pixmap)
        painter.setPen(QColor(200, 200, 200))
        font = QFont()
        font.setPointSize(10)
        painter.setFont(font)
        
        # Tipo do jogo
        game_type = "PS1" if game.folder_type == "POPS" else "PS2"
        text = f"{game.title}\n[{game_type}]\n{game.game_id}"
        
        painter.drawText(pixmap.rect(), Qt.AlignmentFlag.AlignCenter, text)
        painter.end()
        
        self.thumbnail_cache[game.game_id] = pixmap
        return pixmap
    
    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid() or index.row() >= len(self.games):
            return None
        
        game = self.games[index.row()]
        
        if role == Qt.ItemDataRole.DecorationRole:
            return self.load_cover_thumbnail(game)
        
        elif role == Qt.ItemDataRole.DisplayRole:
            return game.title
        
        elif role == Qt.ItemDataRole.ToolTipRole:
            game_type = "PS1 (POPStarter)" if game.folder_type == "POPS" else "PS2 (OPL)"
            return f"Título: {game.title}\nID: {game.game_id}\nTipo: {game_type}\nArquivo: {game.filename}"
        
        elif role == Qt.ItemDataRole.StatusTipRole:
            return game.title
        
        return None


class GameGallery(QMainWindow):
    """Janela principal da galeria de jogos"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("POPStarter/OPL Game Gallery")
        self.setGeometry(100, 100, 1200, 800)
        
        self.current_hd_path = None
        self.setup_ui()
        self.setup_style()
        
        # Tentar encontrar HD automaticamente
        self.auto_detect_hd()
    
    def setup_style(self):
        """Configura estilo visual"""
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1a1a2e;
            }
            QListView {
                background-color: #16213e;
                border: none;
                outline: none;
            }
            QListView::item {
                background-color: #0f3460;
                border-radius: 8px;
                margin: 8px;
                padding: 5px;
            }
            QListView::item:hover {
                background-color: #1a5a8a;
            }
            QListView::item:selected {
                background-color: #2a6a9a;
                border: 2px solid #00a8ff;
            }
            QLabel#header {
                color: #00a8ff;
                font-size: 18px;
                font-weight: bold;
                padding: 10px;
            }
            QLabel#status {
                color: #888;
                font-size: 12px;
            }
            QPushButton {
                background-color: #0f3460;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 15px;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #1a5a8a;
            }
            QComboBox {
                background-color: #0f3460;
                color: white;
                border: 1px solid #2a6a9a;
                border-radius: 5px;
                padding: 5px;
                min-width: 150px;
            }
            QLineEdit {
                background-color: #0f3460;
                color: white;
                border: 1px solid #2a6a9a;
                border-radius: 5px;
                padding: 5px;
            }
            QScrollBar:vertical {
                background-color: #16213e;
                width: 12px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical {
                background-color: #0f3460;
                border-radius: 6px;
                min-height: 20px;
            }
            QMenuBar {
                background-color: #0f3460;
                color: white;
            }
            QMenuBar::item:selected {
                background-color: #1a5a8a;
            }
            QMenu {
                background-color: #0f3460;
                color: white;
            }
        """)
    
    def setup_ui(self):
        """Configura interface"""
        # Widget central
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)
        
        # Header
        header = QLabel("🎮 GALERIA DE JOGOS - POPStarter / OPL")
        header.setObjectName("header")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(header)
        
        # Barra de ferramentas
        toolbar = QHBoxLayout()
        
        self.path_edit = QLineEdit()
        self.path_edit.setPlaceholderText("Caminho do HD ou pasta com estrutura POPS/DVD/CD/ART...")
        toolbar.addWidget(self.path_edit)
        
        self.browse_btn = QPushButton("📁 Selecionar")
        self.browse_btn.clicked.connect(self.browse_hd)
        toolbar.addWidget(self.browse_btn)
        
        self.load_btn = QPushButton("🔄 Carregar Biblioteca")
        self.load_btn.clicked.connect(self.load_library)
        toolbar.addWidget(self.load_btn)
        
        # Filtro por tipo
        toolbar.addWidget(QLabel("Filtrar:"))
        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["Todos", "PS1 (POPStarter)", "PS2 (OPL)"])
        self.filter_combo.currentTextChanged.connect(self.filter_games)
        toolbar.addWidget(self.filter_combo)
        
        # Botão atualizar
        self.refresh_btn = QPushButton("⟳ Atualizar Thumbs")
        self.refresh_btn.clicked.connect(self.refresh_thumbs)
        toolbar.addWidget(self.refresh_btn)
        
        toolbar.addStretch()
        main_layout.addLayout(toolbar)
        
        # Grid de jogos
        self.game_model = GameModel()
        self.game_view = QListView()
        self.game_view.setModel(self.game_model)
        self.game_view.setViewMode(QListView.ViewMode.IconMode)
        self.game_view.setIconSize(QSize(180, 250))
        self.game_view.setGridSize(QSize(200, 300))
        self.game_view.setResizeMode(QListView.ResizeMode.Adjust)
        self.game_view.setMovement(QListView.Movement.Static)
        self.game_view.setSpacing(15)
        self.game_view.setWordWrap(True)
        
        # Double-click abre o jogo (ou pasta)
        self.game_view.doubleClicked.connect(self.on_game_double_click)
        
        main_layout.addWidget(self.game_view)
        
        # Status bar
        self.status_label = QLabel("Pronto - Selecione a pasta do HD")
        self.status_label.setObjectName("status")
        self.statusBar().addWidget(self.status_label)
        
        # Menu
        self.setup_menu()
    
    def setup_menu(self):
        """Configura menu da aplicação"""
        menubar = self.menuBar()
        
        # Menu Arquivo
        file_menu = menubar.addMenu("Arquivo")
        
        open_action = QAction("Abrir HD/Pasta", self)
        open_action.triggered.connect(self.browse_hd)
        open_action.setShortcut("Ctrl+O")
        file_menu.addAction(open_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("Sair", self)
        exit_action.triggered.connect(self.close)
        exit_action.setShortcut("Ctrl+Q")
        file_menu.addAction(exit_action)
        
        # Menu Visualização
        view_menu = menubar.addMenu("Visualização")
        
        zoom_in = QAction("Aumentar Thumbs", self)
        zoom_in.triggered.connect(lambda: self.zoom_thumbs(1.1))
        zoom_in.setShortcut("Ctrl++")
        view_menu.addAction(zoom_in)
        
        zoom_out = QAction("Diminuir Thumbs", self)
        zoom_out.triggered.connect(lambda: self.zoom_thumbs(0.9))
        zoom_out.setShortcut("Ctrl+-")
        view_menu.addAction(zoom_out)
        
        # Menu Ajuda
        help_menu = menubar.addMenu("Ajuda")
        about_action = QAction("Sobre", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def auto_detect_hd(self):
        """Tenta detectar automaticamente o HD com estrutura OPL/POPStarter"""
        common_paths = [
            "/media", "/mnt", "/run/media", 
            str(Path.home()) + "/HDD", "/dev"
        ]
        
        for base in common_paths:
            if os.path.exists(base):
                for item in os.listdir(base):
                    full_path = os.path.join(base, item)
                    if os.path.isdir(full_path):
                        # Verificar se tem estrutura OPL
                        if self.check_opl_structure(full_path):
                            self.path_edit.setText(full_path)
                            self.load_library()
                            return
    
    def check_opl_structure(self, path: str) -> bool:
        """Verifica se o caminho tem estrutura OPL/POPStarter"""
        required_folders = []
        
        # Verificar subpastas comuns
        for folder in os.listdir(path):
            full = os.path.join(path, folder)
            if os.path.isdir(full):
                folder_upper = folder.upper()
                if folder_upper in ['POPS', 'DVD', 'CD', 'ART', 'CFG']:
                    required_folders.append(folder_upper)
        
        # Precisa ter pelo menos POPS ou DVD/CD
        has_pops = 'POPS' in required_folders
        has_games = 'DVD' in required_folders or 'CD' in required_folders
        
        return has_pops or has_games
    
    def browse_hd(self):
        """Abre diálogo para selecionar pasta do HD"""
        folder = QFileDialog.getExistingDirectory(
            self, 
            "Selecione a pasta raiz do HD (com estrutura POPS/DVD/CD/ART)",
            self.path_edit.text() or str(Path.home())
        )
        
        if folder:
            self.path_edit.setText(folder)
            self.load_library()
    
    def load_library(self):
        """Carrega biblioteca de jogos da estrutura do HD"""
        hd_path = self.path_edit.text()
        
        if not hd_path or not os.path.exists(hd_path):
            QMessageBox.warning(self, "Erro", "Caminho inválido! Selecione a pasta do HD.")
            return
        
        self.status_label.setText("Carregando biblioteca... Por favor, aguarde.")
        QApplication.processEvents()
        
        # Limpar modelo atual
        self.game_model.clear()
        
        games_found = 0
        
        # Buscar jogos POPS (PS1)
        pops_path = self.find_folder(hd_path, "POPS")
        if pops_path:
            games_found += self.scan_pops_games(pops_path, hd_path)
        
        # Buscar jogos DVD (PS2 DVD)
        dvd_path = self.find_folder(hd_path, "DVD")
        if dvd_path:
            games_found += self.scan_ps2_games(dvd_path, "DVD", hd_path)
        
        # Buscar jogos CD (PS2 CD)
        cd_path = self.find_folder(hd_path, "CD")
        if cd_path:
            games_found += self.scan_ps2_games(cd_path, "CD", hd_path)
        
        # Buscar pasta ART para capas
        art_path = self.find_folder(hd_path, "ART")
        
        if games_found == 0:
            QMessageBox.information(
                self, 
                "Nenhum jogo encontrado",
                f"Não foram encontrados jogos na estrutura:\n{hd_path}\n\n"
                "Certifique-se que existem pastas: POPS/, DVD/, ou CD/\n"
                "com arquivos .VCD (PS1) ou .iso (PS2)"
            )
        
        self.status_label.setText(f"✅ Biblioteca carregada: {games_found} jogos encontrados")
        self.filter_games()
    
    def find_folder(self, base_path: str, folder_name: str) -> Optional[str]:
        """Procura por uma pasta em base_path ou subpastas"""
        # Verificar na raiz
        direct = os.path.join(base_path, folder_name)
        if os.path.isdir(direct):
            return direct
        
        # Verificar em subpastas (caso esteja dentro de outra estrutura)
        for item in os.listdir(base_path):
            full = os.path.join(base_path, item)
            if os.path.isdir(full):
                sub = os.path.join(full, folder_name)
                if os.path.isdir(sub):
                    return sub
        
        return None
    
    def scan_pops_games(self, pops_path: str, hd_path: str) -> int:
        """Escaneia jogos PS1 na pasta POPS"""
        games_count = 0
        art_base = self.find_folder(hd_path, "ART")
        
        for file in os.listdir(pops_path):
            if file.upper().endswith('.VCD'):
                games_count += 1
                
                # Extrair informações do nome do arquivo
                # Formato comum: SCUS_941.94.Gran Turismo.VCD
                name_parts = file.rsplit('.', 2)
                game_id = name_parts[0] if len(name_parts) > 1 else file
                
                # Extrair título
                title = game_id
                if '.' in game_id:
                    parts = game_id.split('.', 2)
                    if len(parts) >= 3:
                        title = parts[2].replace('_', ' ')
                    elif len(parts) >= 2:
                        title = parts[1]
                
                # Procurar capa na pasta ART
                cover_path = None
                if art_base:
                    # Procurar por arquivo de capa correspondente
                    for ext in ['.jpg', '.png', '.jpeg']:
                        # Nome do arquivo OPL: GAMEID.jpg ou GAMEID.png
                        candidate = os.path.join(art_base, f"{game_id}{ext}")
                        if os.path.exists(candidate):
                            cover_path = candidate
                            break
                        
                        # Tentar com o título
                        title_clean = title.replace(' ', '_')
                        candidate2 = os.path.join(art_base, f"{title_clean}{ext}")
                        if os.path.exists(candidate2):
                            cover_path = candidate2
                            break
                
                game = GameInfo(
                    title=title,
                    game_id=game_id,
                    filename=file,
                    file_ext='.VCD',
                    folder_type='POPS',
                    cover_path=cover_path,
                    disk_art_path=None,
                    screen_path=None
                )
                self.game_model.add_game(game)
        
        return games_count
    
    def scan_ps2_games(self, games_path: str, game_type: str, hd_path: str) -> int:
        """Escaneia jogos PS2 na pasta DVD ou CD"""
        games_count = 0
        art_base = self.find_folder(hd_path, "ART")
        
        for file in os.listdir(games_path):
            if file.upper().endswith('.ISO'):
                games_count += 1
                
                # Extrair informações do nome do arquivo
                # Formato OPL: SLUS_202.02.Game Name.iso
                name_parts = file.rsplit('.', 2)
                game_id = name_parts[0] if len(name_parts) > 1 else file
                
                # Extrair título
                title = game_id
                if '.' in game_id:
                    parts = game_id.split('.', 2)
                    if len(parts) >= 3:
                        title = parts[2].replace('_', ' ')
                    elif len(parts) >= 2:
                        title = parts[1]
                
                # Procurar capa
                cover_path = None
                if art_base:
                    for ext in ['.jpg', '.png', '.jpeg']:
                        candidate = os.path.join(art_base, f"{game_id}{ext}")
                        if os.path.exists(candidate):
                            cover_path = candidate
                            break
                        
                        # Tentar com o título
                        title_clean = title.replace(' ', '_')
                        candidate2 = os.path.join(art_base, f"{title_clean}{ext}")
                        if os.path.exists(candidate2):
                            cover_path = candidate2
                            break
                
                game = GameInfo(
                    title=title,
                    game_id=game_id,
                    filename=file,
                    file_ext='.ISO',
                    folder_type=game_type,
                    cover_path=cover_path,
                    disk_art_path=None,
                    screen_path=None
                )
                self.game_model.add_game(game)
        
        return games_count
    
    def filter_games(self):
        """Filtra jogos por tipo"""
        filter_text = self.filter_combo.currentText()
        
        if filter_text == "Todos":
            for i in range(self.game_model.rowCount()):
                index = self.game_model.index(i)
                self.game_view.setRowHidden(i, False)
        elif filter_text == "PS1 (POPStarter)":
            for i in range(self.game_model.rowCount()):
                game = self.game_model.games[i]
                is_ps1 = (game.folder_type == "POPS")
                self.game_view.setRowHidden(i, not is_ps1)
        elif filter_text == "PS2 (OPL)":
            for i in range(self.game_model.rowCount()):
                game = self.game_model.games[i]
                is_ps2 = (game.folder_type in ["DVD", "CD"])
                self.game_view.setRowHidden(i, not is_ps2)
        
        visible = sum(1 for i in range(self.game_model.rowCount()) 
                     if not self.game_view.isRowHidden(i))
        self.status_label.setText(f"Exibindo {visible} de {self.game_model.rowCount()} jogos")
    
    def zoom_thumbs(self, factor):
        """Aumenta/diminui tamanho dos thumbnails"""
        current = self.game_view.iconSize()
        new_width = int(current.width() * factor)
        new_height = int(current.height() * factor)
        
        if 80 <= new_width <= 400:
            self.game_view.setIconSize(QSize(new_width, new_height))
            self.game_model.cover_size = QSize(new_width, new_height)
            # Limpar cache para regenerar thumbs
            self.game_model.thumbnail_cache.clear()
            self.game_view.update()
    
    def refresh_thumbs(self):
        """Atualiza todos os thumbnails (limpa cache)"""
        self.game_model.thumbnail_cache.clear()
        self.game_view.update()
        self.status_label.setText("Thumbnails atualizados", 2000)
    
    def on_game_double_click(self, index):
        """Ação ao dar double-click no jogo"""
        if not index.isValid():
            return
        
        game = self.game_model.games[index.row()]
        
        # Mostrar informações do jogo
        msg = QMessageBox(self)
        msg.setWindowTitle(game.title)
        msg.setText(f"Jogo: {game.title}\nID: {game.game_id}\nTipo: {game.folder_type}")
        
        if game.cover_path:
            pixmap = QPixmap(game.cover_path)
            if not pixmap.isNull():
                scaled = pixmap.scaled(300, 400, Qt.AspectRatioMode.KeepAspectRatio)
                msg.setIconPixmap(scaled)
        
        msg.setInformativeText("Clique em OK para abrir a pasta do jogo")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        
        if msg.exec() == QMessageBox.StandardButton.Ok:
            # Abrir a pasta onde o jogo está localizado
            hd_path = self.path_edit.text()
            game_folder = self.find_folder(hd_path, game.folder_type)
            if game_folder:
                QDesktopServices.openUrl(QUrl.fromLocalFile(game_folder))
    
    def show_about(self):
        """Mostra informações sobre o aplicativo"""
        QMessageBox.about(
            self,
            "Sobre POPStarter/OPL Game Gallery",
            "POPStarter/OPL Game Gallery v1.0\n\n"
            "Um visualizador de jogos para PC que lê a estrutura do seu HD\n"
            "com jogos para POPStarter (PS1) e OPL (PS2).\n\n"
            "Estrutura suportada:\n"
            "• POPS/ - Jogos PS1 em formato .VCD\n"
            "• DVD/ e CD/ - Jogos PS2 em formato .ISO\n"
            "• ART/ - Capas de jogos (nome do arquivo deve corresponder ao Game ID)\n\n"
            "Desenvolvido com PySide6\n"
            "Estilo inspirado no OpenLoader"
        )


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("POPStarter/OPL Game Gallery")
    
    window = GameGallery()
    window.show()
    
    sys.exit(app.exec())


if __name__ == '__main__':
    main()