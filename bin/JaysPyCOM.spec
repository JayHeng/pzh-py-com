# -*- mode: python -*-

block_cipher = None


a = Analysis(['..\\src\\jayspycom_main.py', '..\\src\\jayspycom_formatter.py', '..\\gui\\jayspycom_win.py'],
             pathex=['D:\\my_git_repo\\JaysPyCOM\\bin'],
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
          name='JaysPyCOM',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='..\\img\\jayspycom.ico')
