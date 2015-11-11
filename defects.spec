# -*- mode: python -*-
a = Analysis(['defects.py'],
             pathex=['P:\\git\\PCInventorySystem'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='defects.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
