"""Reconstrói tudo: tokens -> ícones -> prévias -> .qss -> docs/."""
import subprocess, sys, os
D = os.path.dirname(os.path.abspath(__file__))
for s in ['build_tokens.py', 'build_icons.py', 'build_mockups.py', 'build_components.py', 'build_qss.py', 'render_previews.py']:
    print('>>', s); subprocess.run([sys.executable, os.path.join(D, s)] + (sys.argv[1:] if s == 'render_previews.py' else []), check=True, cwd=D)
