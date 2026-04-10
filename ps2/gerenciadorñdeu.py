#!/usr/bin/env python3
"""
POPStarter/OPL Media Gallery - Visualizador de jogos para PC
Estilo OpenLoader com suporte completo a capas na pasta ART
"""

import sys
import os
from pathlib import Path
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from dataclasses import dataclass
from typing import List, Optional, Dict
import re

# Pastas que NUNCA devem ser escaneadas
PASTAS_BLOQUEADAS = {
    '/dev', '/proc', '/sys', '/run', '/tmp', '/var', '/boot',
    '/dev/', '/proc/', '/sys/', '/run/', '/tmp/', '/var/', '/boot/'
}

@dataclass
class GameInfo:
    """Informações de um jogo"""
    title: str
    game_id: str
    filename: str
    file_ext: str
    folder_type: str
    cover_path: Optional[str]
    disk_art_path: Optional[str]
    screen_path: Optional[str]

class GameModel(QAbstractListModel):
    """Modelo para lista de jogos com cache de thumbnails"""
    
    def __init__(self):
        super().__init__()
        self.games: List[GameInfo] = []
        self.cover_size = QSize(200, 280)
        self.thumbnail_cache: Dict[str, QPixmap] = {}
        self.default_cover = None
        
    def rowCount(self, parent=QModelIndex()):
        return len(self.games)
    
    def add_game(self, game: GameInfo):
        self.beginInsertRows(QModelIndex(), len(self.games), len(self.games))
        self.games.append(game)
        self.endInsertRows()
    
    def clear(self):
        self.beginResetModel()
        self.games.clear()
        self.thumbnail_cache.clear()
        self.endResetModel()
    
    def get_default_cover(self) -> QPixmap:
        """Cria uma capa padrão para jogos sem arte"""
        if self.default_cover is None:
            pixmap = QPixmap(self.cover_size)
            pixmap.fill(QColor(30, 30, 50))
            painter = QPainter(pixmap)
            
            # Fundo gradiente
            gradient = QLinearGradient(0, 0, 0, self.cover_size.height())
            gradient.setColorAt(0, QColor(40, 40, 70))
            gradient.setColorAt(1, QColor(20, 20, 40))
            painter.fillRect(pixmap.rect(), gradient)
            
            # Borda
            painter.setPen(QPen(QColor(80, 80, 120), 2))
            painter.drawRect(2, 2, self.cover_size.width() - 4, self.cover_size.height() - 4)
            
            # Ícone de jogo
            painter.setPen(QColor(150, 150, 200))
            font = QFont("Segoe UI Emoji", 40)
            painter.setFont(font)
            painter.drawText(pixmap.rect(), Qt.AlignmentFlag.AlignCenter, "🎮")
            
            painter.end()
            self.default_cover = pixmap
        
        return self.default_cover
    
    def find_cover_art(self, game: GameInfo, art_folder: str) -> Optional[str]:
        """Procura capa na pasta ART com várias estratégias"""
        if not art_folder or not os.path.exists(art_folder):
            return None
        
        # Lista de possíveis nomes de arquivo para a capa
        possible_names = []
        
        # 1. Game ID puro (ex: SCUS_941.94)
        possible_names.append(game.game_id)
        
        # 2. Game ID sem extensão (ex: SCUS_941.94)
        possible_names.append(game.game_id.split('.')[0] if '.' in game.game_id else game.game_id)
        
        # 3. Título com espaços substituídos por underscore
        title_clean = re.sub(r'[^\w\-_\. ]', '_', game.title)
        possible_names.append(title_clean)
        possible_names.append(title_clean.replace(' ', '_'))
        possible_names.append(title_clean.replace(' ', ''))
        
        # 4. Nome do arquivo sem extensão
        base_name = os.path.splitext(game.filename)[0]
        possible_names.append(base_name)
        
        # 5. Variações comuns de formatação
        if '_' in game.game_id:
            possible_names.append(game.game_id.replace('_', '-'))
            possible_names.append(game.game_id.replace('_', '.'))
        
        # 6. Apenas o código do jogo (ex: SCUS)
        code_parts = game.game_id.split('_')
        if len(code_parts) > 0:
            possible_names.append(code_parts[0])
        
        # Extensões suportadas
        extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp']
        
        # Procurar arquivos
        for name in possible_names:
            for ext in extensions:
                # Nome exato
                candidate = os.path.join(art_folder, f"{name}{ext}")
                if os.path.exists(candidate):
                    return candidate
                
                # Case insensitive
                try:
                    for file in os.listdir(art_folder):
                        if file.lower() == f"{name.lower()}{ext}":
                            return os.path.join(art_folder, file)
                except:
                    pass
        
        # Procurar qualquer arquivo que contenha o Game ID no nome
        try:
            for file in os.listdir(art_folder):
                file_lower = file.lower()
                if game.game_id.lower() in file_lower and file_lower.endswith(tuple(extensions)):
                    return os.path.join(art_folder, file)
        except:
            pass
        
        return None
    
    def load_cover_thumbnail(self, game: GameInfo) -> QPixmap:
        """Carrega e redimensiona a capa do jogo"""
        if game.game_id in self.thumbnail_cache:
            return self.thumbnail_cache[game.game_id]
        
        # Tentar carregar capa
        if game.cover_path and os.path.exists(game.cover_path):
            try:
                pixmap = QPixmap(game.cover_path)
                if not pixmap.isNull():
                    # Redimensionar mantendo proporção
                    scaled = pixmap.scaled(
                        self.cover_size,
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation
                    )
                    
                    # Centralizar em canvas do tamanho exato
                    final = QPixmap(self.cover_size)
                    final.fill(QColor(20, 20, 40))
                    painter = QPainter(final)
                    x = (self.cover_size.width() - scaled.width()) // 2
                    y = (self.cover_size.height() - scaled.height()) // 2
                    painter.drawPixmap(x, y, scaled)
                    painter.end()
                    
                    self.thumbnail_cache[game.game_id] = final
                    return final
            except Exception as e:
                print(f"Erro ao carregar capa {game.cover_path}: {e}")
        
        # Capa padrão se não encontrar
        return self.get_default_cover()
    
    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid() or index.row() >= len(self.games):
            return None
        
        game = self.games[index.row()]
        
        if role == Qt.ItemDataRole.DecorationRole:
            return self.load_cover_thumbnail(game)
        
        elif role == Qt.ItemDataRole.DisplayRole:
            # Mostrar título e tipo
            game_type = "PS1" if game.folder_type == "POPS" else "PS2"
            return f"{game.title}\n[{game_type}]"
        
        elif role == Qt.ItemDataRole.ToolTipRole:
            game_type = "PS1 (POPStarter)" if game.folder_type == "POPS" else "PS2 (OPL)"
            has_cover = "✓" if game.cover_path and os.path.exists(game.cover_path) else "✗"
            return (f"🎮 {game.title}\n"
                   f"📋 ID: {game.game_id}\n"
                   f"📀 Tipo: {game_type}\n"
                   f"📁 Arquivo: {game.filename}\n"
                   f"🖼️ Capa: {has_cover}")
        
        elif role == Qt.ItemDataRole.TextAlignmentRole:
            return Qt.AlignmentFlag.AlignCenter
        
        return None


class GameGallery(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("POPStarter/OPL Game Gallery - OpenLoader Style")
        self.setGeometry(100, 100, 1300, 850)
        
        self.current_hd_path = None
        self.setup_ui()
        self.setup_style()
        
        # Carregar último caminho usado se existir
        self.load_settings()
        
        QTimer.singleShot(500, self.auto_detect_hd)
    
    def setup_style(self):
        """Estilo visual inspirado no OpenLoader"""
        self.setStyleSheet("""
            QMainWindow {
                background-color: #0a0e1a;
            }
            QListView {
                background-color: #0f1420;
                border: none;
                outline: none;
                padding: 10px;
            }
            QListView::item {
                background-color: #1a1f2e;
                border-radius: 10px;
                margin: 8px;
                padding: 8px;
            }
            QListView::item:hover {
                background-color: #252a3e;
                border: 1px solid #4a6fa5;
            }
            QListView::item:selected {
                background-color: #2a3a5e;
                border: 2px solid #6ea8fe;
            }
            QLabel#header {
                color: #6ea8fe;
                font-size: 20px;
                font-weight: bold;
                padding: 15px;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #0a0e1a, stop:1 #1a1f2e);
                border-bottom: 2px solid #2a3a5e;
            }
            QLabel#status {
                color: #8899bb;
                font-size: 12px;
                padding: 5px;
            }
            QPushButton {
                background-color: #1a1f2e;
                color: #6ea8fe;
                border: 1px solid #2a3a5e;
                border-radius: 6px;
                padding: 8px 15px;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2a3a5e;
                color: #8eb8fe;
                border-color: #4a6fa5;
            }
            QPushButton:pressed {
                background-color: #0f1420;
            }
            QLineEdit {
                background-color: #0f1420;
                color: #ccddff;
                border: 1px solid #2a3a5e;
                border-radius: 6px;
                padding: 8px;
                font-size: 13px;
            }
            QLineEdit:focus {
                border-color: #6ea8fe;
            }
            QComboBox {
                background-color: #1a1f2e;
                color: #ccddff;
                border: 1px solid #2a3a5e;
                border-radius: 6px;
                padding: 6px;
                min-width: 150px;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 5px solid #6ea8fe;
                margin-right: 5px;
            }
            QComboBox QAbstractItemView {
                background-color: #1a1f2e;
                color: #ccddff;
                selection-background-color: #2a3a5e;
                border: 1px solid #2a3a5e;
            }
            QScrollBar:vertical {
                background-color: #0f1420;
                width: 10px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background-color: #2a3a5e;
                border-radius: 5px;
                min-height: 20px;
            }
            QScrollBar::handle:vertical:hover {
                background-color: #4a6fa5;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
            QMenuBar {
                background-color: #0a0e1a;
                color: #ccddff;
                border-bottom: 1px solid #1a1f2e;
            }
            QMenuBar::item:selected {
                background-color: #1a1f2e;
            }
            QMenu {
                background-color: #1a1f2e;
                color: #ccddff;
                border: 1px solid #2a3a5e;
            }
            QMenu::item:selected {
                background-color: #2a3a5e;
            }
            QProgressBar {
                background-color: #0f1420;
                border: 1px solid #2a3a5e;
                border-radius: 4px;
                text-align: center;
                color: #ccddff;
            }
            QProgressBar::chunk {
                background-color: #4a6fa5;
                border-radius: 3px;
            }
            QStatusBar {
                background-color: #0a0e1a;
                color: #8899bb;
            }
        """)
    
    def setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Header
        header = QLabel("🎮 POPStarter / OPL GAME GALLERY 🎮")
        header.setObjectName("header")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(header)
        
        # Toolbar container
        toolbar_widget = QWidget()
        toolbar_widget.setStyleSheet("background-color: #0f1420; padding: 10px;")
        toolbar_layout = QHBoxLayout(toolbar_widget)
        
        self.path_edit = QLineEdit()
        self.path_edit.setPlaceholderText("📁 Selecione a pasta do HD com estrutura POPS/DVD/CD/ART...")
        toolbar_layout.addWidget(self.path_edit)
        
        self.browse_btn = QPushButton("📂 SELECIONAR")
        self.browse_btn.clicked.connect(self.browse_hd)
        toolbar_layout.addWidget(self.browse_btn)
        
        self.load_btn = QPushButton("🔄 CARREGAR")
        self.load_btn.clicked.connect(self.load_library)
        toolbar_layout.addWidget(self.load_btn)
        
        toolbar_layout.addWidget(QLabel("Filtrar:"))
        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["🎮 Todos os Jogos", "🎮 PS1 (POPStarter)", "🎮 PS2 (OPL)"])
        self.filter_combo.currentTextChanged.connect(self.filter_games)
        toolbar_layout.addWidget(self.filter_combo)
        
        self.refresh_btn = QPushButton("🖼️ ATUALIZAR CAPAS")
        self.refresh_btn.clicked.connect(self.refresh_thumbs)
        toolbar_layout.addWidget(self.refresh_btn)
        
        # Info label
        self.info_label = QLabel("📊 0 jogos")
        self.info_label.setStyleSheet("color: #6ea8fe; padding: 0 10px;")
        toolbar_layout.addWidget(self.info_label)
        
        toolbar_layout.addStretch()
        main_layout.addWidget(toolbar_widget)
        
        # Grid de jogos
        self.game_model = GameModel()
        self.game_view = QListView()
        self.game_view.setModel(self.game_model)
        self.game_view.setViewMode(QListView.ViewMode.IconMode)
        self.game_view.setIconSize(QSize(200, 280))
        self.game_view.setGridSize(QSize(220, 320))
        self.game_view.setResizeMode(QListView.ResizeMode.Adjust)
        self.game_view.setMovement(QListView.Movement.Static)
        self.game_view.setSpacing(15)
        self.game_view.setWordWrap(True)
        self.game_view.setFlow(QListView.Flow.LeftToRight)
        self.game_view.setWrapping(True)
        self.game_view.doubleClicked.connect(self.on_game_double_click)
        
        main_layout.addWidget(self.game_view)
        
        # Status bar
        self.status_label = QLabel("✅ Pronto - Selecione a pasta do HD com os jogos")
        self.status_label.setObjectName("status")
        self.statusBar().addWidget(self.status_label)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setMaximumWidth(200)
        self.statusBar().addPermanentWidget(self.progress_bar)
        
        self.setup_menu()
    
    def setup_menu(self):
        menubar = self.menuBar()
        
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
        
        view_menu = menubar.addMenu("Visualização")
        zoom_in = QAction("Aumentar Capas", self)
        zoom_in.triggered.connect(lambda: self.zoom_thumbs(1.1))
        zoom_in.setShortcut("Ctrl++")
        view_menu.addAction(zoom_in)
        
        zoom_out = QAction("Diminuir Capas", self)
        zoom_out.triggered.connect(lambda: self.zoom_thumbs(0.9))
        zoom_out.setShortcut("Ctrl+-")
        view_menu.addAction(zoom_out)
        
        view_menu.addSeparator()
        
        reset_zoom = QAction("Tamanho Normal", self)
        reset_zoom.triggered.connect(lambda: self.set_zoom(200))
        reset_zoom.setShortcut("Ctrl+0")
        view_menu.addAction(reset_zoom)
        
        help_menu = menubar.addMenu("Ajuda")
        about_action = QAction("Sobre", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def load_settings(self):
        """Carrega configurações salvas"""
        settings = QSettings("POPStarterGallery", "GameGallery")
        last_path = settings.value("last_path", "")
        if last_path and os.path.exists(last_path):
            self.path_edit.setText(last_path)
    
    def save_settings(self):
        """Salva configurações"""
        settings = QSettings("POPStarterGallery", "GameGallery")
        settings.setValue("last_path", self.path_edit.text())
    
    def is_path_blocked(self, path: str) -> bool:
        """Verifica se o caminho deve ser bloqueado"""
        path_normalized = str(path).rstrip('/')
        
        for blocked in PASTAS_BLOQUEADAS:
            if path_normalized == blocked.rstrip('/') or path_normalized.startswith(blocked):
                return True
        
        if path_normalized.startswith('/dev'):
            return True
        
        return False
    
    def auto_detect_hd(self):
        """Detecta automaticamente HD com jogos"""
        common_paths = ["/media", "/mnt", "/run/media", str(Path.home())]
        
        for base in common_paths:
            if not os.path.exists(base) or self.is_path_blocked(base):
                continue
            
            try:
                with os.scandir(base) as iterator:
                    for entry in iterator:
                        if entry.is_dir() and os.access(entry.path, os.R_OK):
                            if not self.is_path_blocked(entry.path):
                                if self.check_opl_structure(entry.path):
                                    self.path_edit.setText(entry.path)
                                    self.load_library()
                                    return
            except:
                continue
    
    def check_opl_structure(self, path: str) -> bool:
        """Verifica estrutura OPL"""
        if self.is_path_blocked(path) or not os.access(path, os.R_OK):
            return False
        
        try:
            with os.scandir(path) as iterator:
                folders = [entry.name.upper() for entry in iterator if entry.is_dir()]
                return 'POPS' in folders or 'DVD' in folders or 'CD' in folders
        except:
            return False
    
    def browse_hd(self):
        folder = QFileDialog.getExistingDirectory(
            self, 
            "Selecione a pasta raiz do HD (com POPS/DVD/CD/ART)",
            self.path_edit.text() or str(Path.home())
        )
        
        if folder and not self.is_path_blocked(folder):
            self.path_edit.setText(folder)
            self.save_settings()
            self.load_library()
    
    def load_library(self):
        hd_path = self.path_edit.text()
        
        if not hd_path or not os.path.exists(hd_path):
            QMessageBox.warning(self, "Erro", "Caminho inválido!")
            return
        
        if self.is_path_blocked(hd_path):
            QMessageBox.warning(self, "Erro", f"Caminho bloqueado: {hd_path}")
            return
        
        if not os.access(hd_path, os.R_OK):
            reply = QMessageBox.question(self, "Permissão", 
                f"Sem permissão para ler {hd_path}\n\nDeseja tentar com sudo?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                os.system(f"sudo chmod -R +r {hd_path}")
                self.load_library()
            return
        
        self.status_label.setText("🔄 Carregando biblioteca...")
        self.progress_bar.setVisible(True)
        self.progress_bar.setRange(0, 0)
        QApplication.processEvents()
        
        self.game_model.clear()
        
        games_found = 0
        
        # Encontrar pasta ART
        art_path = self.find_folder(hd_path, "ART")
        
        # POPS (PS1)
        pops_path = self.find_folder(hd_path, "POPS")
        if pops_path:
            games_found += self.scan_games(pops_path, "POPS", art_path)
        
        # DVD (PS2)
        dvd_path = self.find_folder(hd_path, "DVD")
        if dvd_path:
            games_found += self.scan_games(dvd_path, "DVD", art_path)
        
        # CD (PS2)
        cd_path = self.find_folder(hd_path, "CD")
        if cd_path:
            games_found += self.scan_games(cd_path, "CD", art_path)
        
        self.progress_bar.setVisible(False)
        
        if games_found == 0:
            QMessageBox.information(self, "Nenhum jogo", 
                f"Nenhum jogo encontrado em:\n{hd_path}\n\n"
                "Estrutura esperada:\n"
                "📁 HD/\n"
                "  📁 POPS/     (arquivos .VCD do PS1)\n"
                "  📁 DVD/      (arquivos .ISO do PS2 DVD)\n"
                "  📁 CD/       (arquivos .ISO do PS2 CD)\n"
                "  📁 ART/      (capas .jpg/.png)")
        
        self.info_label.setText(f"📊 {games_found} jogos")
        self.status_label.setText(f"✅ {games_found} jogos carregados!")
        self.filter_games()
        self.save_settings()
    
    def find_folder(self, base_path: str, folder_name: str) -> Optional[str]:
        """Procura pasta case-insensitive"""
        try:
            with os.scandir(base_path) as iterator:
                for entry in iterator:
                    if entry.is_dir() and entry.name.upper() == folder_name.upper():
                        return entry.path
                    
                    # Procurar em subpastas (1 nível)
                    if entry.is_dir():
                        try:
                            with os.scandir(entry.path) as sub_iter:
                                for sub_entry in sub_iter:
                                    if sub_entry.is_dir() and sub_entry.name.upper() == folder_name.upper():
                                        return sub_entry.path
                        except:
                            continue
        except:
            pass
        return None
    
    def scan_games(self, games_path: str, game_type: str, art_path: str) -> int:
        """Escaneia jogos em uma pasta"""
        games_count = 0
        extensions = ['.VCD', '.ISO'] if game_type == 'POPS' else ['.ISO']
        
        try:
            with os.scandir(games_path) as iterator:
                for entry in iterator:
                    if entry.is_file() and entry.name.upper().endswith(tuple(extensions)):
                        games_count += 1
                        
                        filename = entry.name
                        
                        # Extrair Game ID e título
                        name_without_ext = os.path.splitext(filename)[0]
                        
                        # Tentar extrair ID no formato XXXXX_XXX.XX
                        id_match = re.search(r'([A-Z]{4,5}_\d{3,4}\.\d{2})', name_without_ext)
                        if id_match:
                            game_id = id_match.group(1)
                            # Título é o resto depois do ID
                            title_parts = name_without_ext.split(game_id, 1)
                            title = title_parts[1].strip(' ._-') if len(title_parts) > 1 else game_id
                        else:
                            game_id = name_without_ext[:20]
                            title = name_without_ext
                        
                        # Limpar título
                        title = re.sub(r'[^\w\s\-]', '', title).strip()
                        if not title:
                            title = game_id
                        
                        # Procurar capa
                        cover_path = self.game_model.find_cover_art(
                            GameInfo(title, game_id, filename, '', game_type, None, None, None),
                            art_path
                        ) if art_path else None
                        
                        game = GameInfo(
                            title=title,
                            game_id=game_id,
                            filename=filename,
                            file_ext=extensions[0],
                            folder_type=game_type,
                            cover_path=cover_path,
                            disk_art_path=None,
                            screen_path=None
                        )
                        self.game_model.add_game(game)
                        
                        if games_count % 20 == 0:
                            QApplication.processEvents()
        except Exception as e:
            print(f"Erro em {game_type}: {e}")
        
        return games_count
    
    def filter_games(self):
        filter_text = self.filter_combo.currentText()
        
        for i in range(self.game_model.rowCount()):
            game = self.game_model.games[i]
            
            if "PS1" in filter_text:
                self.game_view.setRowHidden(i, game.folder_type != "POPS")
            elif "PS2" in filter_text:
                self.game_view.setRowHidden(i, game.folder_type not in ["DVD", "CD"])
            else:
                self.game_view.setRowHidden(i, False)
        
        visible = sum(1 for i in range(self.game_model.rowCount()) 
                     if not self.game_view.isRowHidden(i))
        self.status_label.setText(f"🎮 Exibindo {visible} de {self.game_model.rowCount()} jogos")
        self.info_label.setText(f"📊 {self.game_model.rowCount()} jogos | 👁️ {visible} visíveis")
    
    def zoom_thumbs(self, factor):
        current = self.game_view.iconSize()
        new_size = int(current.width() * factor)
        self.set_zoom(new_size)
    
    def set_zoom(self, size):
        size = max(100, min(350, size))
        new_height = int(size * 1.4)
        self.game_view.setIconSize(QSize(size, new_height))
        self.game_view.setGridSize(QSize(size + 20, new_height + 40))
        self.game_model.cover_size = QSize(size, new_height)
        self.game_model.thumbnail_cache.clear()
        self.game_view.update()
    
    def refresh_thumbs(self):
        self.game_model.thumbnail_cache.clear()
        self.game_view.update()
        self.status_label.setText("🖼️ Capas recarregadas!")
        QTimer.singleShot(2000, lambda: self.status_label.setText("✅ Pronto"))
    
    def on_game_double_click(self, index):
        if not index.isValid():
            return
        
        game = self.game_model.games[index.row()]
        
        msg = QMessageBox(self)
        msg.setWindowTitle(f"🎮 {game.title}")
        msg.setText(f"<b>{game.title}</b><br>"
                   f"ID: {game.game_id}<br>"
                   f"Tipo: {'PS1 (POPStarter)' if game.folder_type == 'POPS' else 'PS2 (OPL)'}<br>"
                   f"Arquivo: {game.filename}")
        
        if game.cover_path and os.path.exists(game.cover_path):
            pixmap = QPixmap(game.cover_path)
            if not pixmap.isNull():
                scaled = pixmap.scaled(250, 350, Qt.AspectRatioMode.KeepAspectRatio)
                msg.setIconPixmap(scaled)
        
        msg.setInformativeText("Clique em OK para abrir a pasta do jogo")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        
        if msg.exec() == QMessageBox.StandardButton.Ok:
            hd_path = self.path_edit.text()
            game_folder = self.find_folder(hd_path, game.folder_type)
            if game_folder:
                QDesktopServices.openUrl(QUrl.fromLocalFile(game_folder))
    
    def show_about(self):
        QMessageBox.about(
            self,
            "Sobre",
            "<h2>POPStarter/OPL Game Gallery</h2>"
            "<p>Visualizador de jogos estilo OpenLoader para PC</p>"
            "<p><b>Versão:</b> 1.0</p>"
            "<p><b>Funcionalidades:</b></p>"
            "<ul>"
            "<li>Leitura automática da estrutura POPS/DVD/CD/ART</li>"
            "<li>Suporte a capas nos formatos JPG, PNG, GIF, WEBP</li>"
            "<li>Filtro por tipo de jogo (PS1/PS2)</li>"
            "<li>Zoom nas capas (Ctrl+ / Ctrl-)</li>"
            "<li>Interface escura estilo OpenLoader</li>"
            "</ul>"
            "<p><b>Desenvolvido com:</b> PySide6</p>"
        )


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("POPStarter/OPL Game Gallery")
    app.setOrganizationName("GameGallery")
    
    window = GameGallery()
    window.show()
    
    sys.exit(app.exec())


if __name__ == '__main__':
    main()