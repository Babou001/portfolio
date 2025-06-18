from pathlib import Path
import sys
import types

# Ensure the repository root is on sys.path
root_path = Path(__file__).resolve().parents[1]
if str(root_path) not in sys.path:
    sys.path.insert(0, str(root_path))

class DummyObj:
    def __getattr__(self, name):
        return lambda *args, **kwargs: DummyObj()
    def __call__(self, *args, **kwargs):
        return DummyObj()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc, tb):
        pass

streamlit = types.ModuleType('streamlit')
streamlit.set_page_config = lambda *a, **kw: None
streamlit.markdown = lambda *a, **kw: None
streamlit.title = lambda *a, **kw: None
streamlit.badge = lambda *a, **kw: None
streamlit.image = lambda *a, **kw: None
streamlit.columns = lambda n: [DummyObj() for _ in range(n)]
streamlit.container = lambda *a, **kw: DummyObj()
streamlit.expander = lambda *a, **kw: DummyObj()
streamlit.popover = lambda *a, **kw: DummyObj()

streamlit_lottie = types.ModuleType('streamlit_lottie')
streamlit_lottie.st_lottie = lambda *a, **kw: None

sys.modules.setdefault('streamlit', streamlit)
sys.modules.setdefault('streamlit_lottie', streamlit_lottie)

import portfolio


def test_style_css_exists():
    css_path = Path(portfolio.__file__).with_name("style.css")
    assert css_path.is_file()

