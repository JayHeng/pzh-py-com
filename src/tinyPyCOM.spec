# -*- mode: python -*-

block_cipher = None


a = Analysis(['tinypycom_main.py', 'tinypycom_formatter.py', '..\\gui\\tinypycom_win.py'],
             pathex=['D:\\my_git_repo\\tinyPyCOM\\src'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='tinyPyCOM',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='..\\img\\tinypycom.ico')
