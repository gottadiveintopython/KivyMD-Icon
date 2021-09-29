if __name__ == 'kivymd':
    def register_icon_font():
        from pathlib import Path
        from kivy.core.text import LabelBase
        font_path = Path(__file__).parent.joinpath('fonts', 'materialdesignicons-webfont.ttf')
        assert font_path.exists()
        LabelBase.register('Icons', str(font_path))
    register_icon_font()
