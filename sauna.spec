# -*- mode: python -*-

block_cipher = None

a = Analysis(['scripts/main'],
             pathex=['/sauna'],
             hiddenimports=['sauna.commands.ext', 'sauna.plugins.ext', 'sauna.consumers.ext'],
             hookspath=None,
             runtime_hooks=['scripts/hook.py'],
             cipher=block_cipher)

pyz = PYZ(a.pure, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='sauna',
          debug=False,
          strip=None,
          upx=True,
          console=True )
