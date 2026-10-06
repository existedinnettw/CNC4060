# DIY CNC router with work area around 400x600mm 

Hi everyone! It's my first attempt to model CNC router in CAD software. Work still in progress, but CAD pretty much done. 

![image](https://github.com/Shkolik/CNC4060/raw/main/docs/Full%20assembly.png)

# Materials

Router made of 10 series fractional aluminum extrusion profiles and aluminum flat stock. Base made of 2 2"x4" side profiles and 4 2"x2" cross members. Gantry made of 2 2"x2" profiles that tied together with 1/2" aluminum plate. All sizes and shapes made to fit widely available flat stock.

Fasteners are mix of metric and imperial threads just because all linear motion hardware use metric, but fractional extrusion wants imperial. You can use all metric, but it will require some additional work.


# CAD

Project created in FreeCAD Link. You can find latest releases here: https://github.com/realthunder/FreeCAD_assembly3/releases

Also you need to install Fasteners workbench: https://github.com/shaise/FreeCAD_FastenersWB

To open project without errors and broken links please maintain folders structure as-is.

## Opening with fcppm (FreeCAD 1.1)

The workbenches the documents need are locked per project by [fcppm](https://github.com/existedinnettw/fcppm): Assembly3 (every assembly), Fasteners (screws in the axes) and Assembly3's `py-slvs` solver. No Addon Manager install is needed.

fcppm and `freecad-fasteners` (packaged from upstream's `V0.5.67-beta` release by [fcppm_recipes](https://github.com/existedinnettw/fcppm_recipes)) come from the `inkr` Gitea index (`https://gitea.insleker.org/api/packages/inkr_org/pypi/simple/`, configured in `~/.config/uv/uv.toml` or `UV_INDEX`; log in once with `uv auth login gitea.insleker.org`); Assembly3 from its git repository and `py-slvs` from PyPI. Versions are pinned in `uv.lock`.

```bash
uv sync --locked                       # builds py-slvs from source on Python 3.14 (SWIG comes from PyPI)
uv run fcppm sync                      # 3rd/freecad-fasteners, FreeCAD.cfg
uv run fcppm run cads/4060CNC.FCStd    # FreeCAD with the locked Assembly3 and Fasteners
```

`uv run fcppm doctor` checks that every link and every Python object in `cads/` resolves. With mainline FreeCAD 1.1, recomputing reports three broken Assembly3 elements (`X_axis_plates#_Element035`, `Z_axis#Element011`, `Z_axis#Element061`): their geometry references were saved by FreeCAD Link (2021) and need re-picking once.

## Disclaimer

This project provided as-is. You can use it to create you own CNC, but there is no guarantee that it will work as you want and will not produce any loss or injury. 
**Work still in progress!** 

If you have any suggestions - post them as issue inside this repo.
