# -*- mode: python -*-

block_cipher = None

a = Analysis(['start.py'],
             pathex=['.'],
             binaries=[],
             datas=[
                 ('splash_img.png', '.'),
                 ('config_default.yml', '.'),
                 ('init.py', '.'),
                 ('app', 'app'),
                 ('helpers', 'helpers'),
                 ('locators', 'locators'),
                 ('pages', 'pages'),
                 ('scenarios', 'scenarios'),
                 ('chromedriver', 'chromedriver'),
             ],
             hiddenimports=[],
             hookspath=['hooks/'],
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
          name='hand_helper',
          debug=False,
          strip=False,
          upx=True,
          console=True)

app = BUNDLE(exe,
             name='hand_helper.app',
             icon=None,
             bundle_identifier=None,
             info_plist={
                 'NSHighResolutionCapable': 'True'
             }
             )
