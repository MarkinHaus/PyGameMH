
import PyInstaller.__main__
filename = ""
name = ""
do = f"{filename}.py" \
     "--distpath .\ --workpath .\Bundel_specs --onedir --onefile --specpath .\exicutable -p .\util --hidden-import " \
     "pumunk --collect-all .\util"\ 
     f" --add-data=image1.png:img \ -n {name}"
PyInstaller.__main__.run([do])
