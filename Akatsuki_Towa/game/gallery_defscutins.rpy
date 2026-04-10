# Cutin images come out with inverted(?) alpha channels
# As of Ren'Py version 8.5.2, this works to reverse it back.
init python:
    import _renpy

    reverse_identity = im.ramp(255,0)

    #Figured out by copying the built-in im.AlphaMask behavior
    class ReverseAlphaMask(im.ImageBase):

        def __init__(self, img):
            super().__init__(img)

            self.img = im.image(img)

        def get_hash(self):
            return self.img.get_hash()

        def load(self):

            surf = im.cache.get(self.img)

            rv = renpy.display.pgrender.copy_surface(surf)

            #Figured out by copying renpy.display.module.alpha_munge behavior
            _renpy.alpha_munge(surf, rv, 3, 3, reverse_identity)

            return rv

        def predict_files(self):
            return self.img.predict_files()


image oc000_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("oc000.png"))
    xysize (None,480)
    fit "contain"

image oc001_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("oc001.png"))
    xysize (None,480)
    fit "contain"

image oc002_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("oc002.png"))
    xysize (None,480)
    fit "contain"

image oc003_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("oc003.png"))
    xysize (None,480)
    fit "contain"

image oc004_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("oc004.png"))
    xysize (None,480)
    fit "contain"

image oc006_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("oc006.png"))
    xysize (None,480)
    fit "contain"

image oc007_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("oc007.png"))
    xysize (None,480)
    fit "contain"

image oc008_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("oc008.png"))
    xysize (None,480)
    fit "contain"

image oca00_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("oca00.png"))
    xysize (None,480)
    fit "contain"

image oca01_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("oca01.png"))
    xysize (None,480)
    fit "contain"

image oca02_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("oca02.png"))
    xysize (None,480)
    fit "contain"

image oca03_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("oca03.png"))
    xysize (None,480)
    fit "contain"

image oca04_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("oca04.png"))
    xysize (None,480)
    fit "contain"

image oca06_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("oca06.png"))
    xysize (None,480)
    fit "contain"

image ocb00_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("ocb00.png"))
    xysize (None,480)
    fit "contain"

image ocb01_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("ocb01.png"))
    xysize (None,480)
    fit "contain"

image ocb02_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("ocb02.png"))
    xysize (None,480)
    fit "contain"

image ocb03_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("ocb03.png"))
    xysize (None,480)
    fit "contain"

image ocb04_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("ocb04.png"))
    xysize (None,480)
    fit "contain"

image ocb06_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("ocb06.png"))
    xysize (None,480)
    fit "contain"

image occ02_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("occ02.png"))
    xysize (None,480)
    fit "contain"

image occ04_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("occ04.png"))
    xysize (None,480)
    fit "contain"

image sc001_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc001.png"))
    xysize (None,480)
    fit "contain"

image sc002_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc002.png"))
    xysize (None,480)
    fit "contain"

image sc003_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc003.png"))
    xysize (None,480)
    fit "contain"

image sc004_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc004.png"))
    xysize (None,480)
    fit "contain"

image sc005_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc005.png"))
    xysize (None,480)
    fit "contain"

image sc006_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc006.png"))
    xysize (None,480)
    fit "contain"

image sc007_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc007.png"))
    xysize (None,480)
    fit "contain"

image sc008_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc008.png"))
    xysize (None,480)
    fit "contain"

image sc009_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc009.png"))
    xysize (None,480)
    fit "contain"

image sc010_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc010.png"))
    xysize (None,480)
    fit "contain"

image sc011_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc011.png"))
    xysize (None,480)
    fit "contain"

image sc012_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc012.png"))
    xysize (None,480)
    fit "contain"

image sc013_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc013.png"))
    xysize (None,480)
    fit "contain"

image sc014_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc014.png"))
    xysize (None,480)
    fit "contain"

image sc015_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc015.png"))
    xysize (None,480)
    fit "contain"

image sc016_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc016.png"))
    xysize (None,480)
    fit "contain"

image sc017_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc017.png"))
    xysize (None,480)
    fit "contain"

image sc018_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc018.png"))
    xysize (None,480)
    fit "contain"

image sc019_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc019.png"))
    xysize (None,480)
    fit "contain"

image sc020_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc020.png"))
    xysize (None,480)
    fit "contain"

image sc021_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc021.png"))
    xysize (None,480)
    fit "contain"

image sc022_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc022.png"))
    xysize (None,480)
    fit "contain"

image sc023_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc023.png"))
    xysize (None,480)
    fit "contain"

image sc024_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc024.png"))
    xysize (None,480)
    fit "contain"

image sc025_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc025.png"))
    xysize (None,480)
    fit "contain"

image sc026_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc026.png"))
    xysize (None,480)
    fit "contain"

image sc027_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc027.png"))
    xysize (None,480)
    fit "contain"

image sc028_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc028.png"))
    xysize (None,480)
    fit "contain"

image sc029_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc029.png"))
    xysize (None,480)
    fit "contain"

image sc030_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc030.png"))
    xysize (None,480)
    fit "contain"

image sc031_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc031.png"))
    xysize (None,480)
    fit "contain"

image sc032_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc032.png"))
    xysize (None,480)
    fit "contain"

image sc033_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc033.png"))
    xysize (None,480)
    fit "contain"

image sc034_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc034.png"))
    xysize (None,480)
    fit "contain"

image sc035_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc035.png"))
    xysize (None,480)
    fit "contain"

image sc036_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc036.png"))
    xysize (None,480)
    fit "contain"

image sc038_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc038.png"))
    xysize (None,480)
    fit "contain"

image sc039_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc039.png"))
    xysize (None,480)
    fit "contain"

image sc040_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc040.png"))
    xysize (None,480)
    fit "contain"

image sc041_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc041.png"))
    xysize (None,480)
    fit "contain"

image sc042_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc042.png"))
    xysize (None,480)
    fit "contain"

image sc043_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc043.png"))
    xysize (None,480)
    fit "contain"

image sc044_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc044.png"))
    xysize (None,480)
    fit "contain"

image sc045_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc045.png"))
    xysize (None,480)
    fit "contain"

image sc046_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc046.png"))
    xysize (None,480)
    fit "contain"

image sc047_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc047.png"))
    xysize (None,480)
    fit "contain"

image sc048_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc048.png"))
    xysize (None,480)
    fit "contain"

image sc049_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc049.png"))
    xysize (None,480)
    fit "contain"

image sc050_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc050.png"))
    xysize (None,480)
    fit "contain"

image sc051_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc051.png"))
    xysize (None,480)
    fit "contain"

image sc052_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc052.png"))
    xysize (None,480)
    fit "contain"

image sc053_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc053.png"))
    xysize (None,480)
    fit "contain"

image sc054_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc054.png"))
    xysize (None,480)
    fit "contain"

image sc055_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc055.png"))
    xysize (None,480)
    fit "contain"

image sc058_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc058.png"))
    xysize (None,480)
    fit "contain"

image sc059_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc059.png"))
    xysize (None,480)
    fit "contain"

image sc060_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc060.png"))
    xysize (None,480)
    fit "contain"

image sc062_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc062.png"))
    xysize (None,480)
    fit "contain"

image sc063_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc063.png"))
    xysize (None,480)
    fit "contain"

image sc064_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc064.png"))
    xysize (None,480)
    fit "contain"

image sc065_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc065.png"))
    xysize (None,480)
    fit "contain"

image sc066_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc066.png"))
    xysize (None,480)
    fit "contain"

image sc067_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc067.png"))
    xysize (None,480)
    fit "contain"

image sc068_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc068.png"))
    xysize (None,480)
    fit "contain"

image sc069_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc069.png"))
    xysize (None,480)
    fit "contain"

image sc070_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc070.png"))
    xysize (None,480)
    fit "contain"

image sc071_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc071.png"))
    xysize (None,480)
    fit "contain"

image sc080_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc080.png"))
    xysize (None,480)
    fit "contain"

image sc081_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc081.png"))
    xysize (None,480)
    fit "contain"

image sc082_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc082.png"))
    xysize (None,480)
    fit "contain"

image sc083_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc083.png"))
    xysize (None,480)
    fit "contain"

image sc084_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc084.png"))
    xysize (None,480)
    fit "contain"

image sc085_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc085.png"))
    xysize (None,480)
    fit "contain"

image sc086_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc086.png"))
    xysize (None,480)
    fit "contain"

image sc087_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc087.png"))
    xysize (None,480)
    fit "contain"

image sc088_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc088.png"))
    xysize (None,480)
    fit "contain"

image sc089_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc089.png"))
    xysize (None,480)
    fit "contain"

image sc090_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc090.png"))
    xysize (None,480)
    fit "contain"

image sc091_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc091.png"))
    xysize (None,480)
    fit "contain"

image sc092_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc092.png"))
    xysize (None,480)
    fit "contain"

image sc093_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc093.png"))
    xysize (None,480)
    fit "contain"

image sc094_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc094.png"))
    xysize (None,480)
    fit "contain"

image sc095_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc095.png"))
    xysize (None,480)
    fit "contain"

image sc096_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc096.png"))
    xysize (None,480)
    fit "contain"

image sc097_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc097.png"))
    xysize (None,480)
    fit "contain"

image sc098_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc098.png"))
    xysize (None,480)
    fit "contain"

image sc099_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc099.png"))
    xysize (None,480)
    fit "contain"

image sc100_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc100.png"))
    xysize (None,480)
    fit "contain"

image sc101_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc101.png"))
    xysize (None,480)
    fit "contain"

image sc102_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc102.png"))
    xysize (None,480)
    fit "contain"

image sc103_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc103.png"))
    xysize (None,480)
    fit "contain"

image sc104_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc104.png"))
    xysize (None,480)
    fit "contain"

image sc105_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc105.png"))
    xysize (None,480)
    fit "contain"

image sc106_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc106.png"))
    xysize (None,480)
    fit "contain"

image sc107_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc107.png"))
    xysize (None,480)
    fit "contain"

image sc108_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc108.png"))
    xysize (None,480)
    fit "contain"

image sc109_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc109.png"))
    xysize (None,480)
    fit "contain"

image sc110_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc110.png"))
    xysize (None,480)
    fit "contain"

image sc111_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc111.png"))
    xysize (None,480)
    fit "contain"

image sc113_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sc113.png"))
    xysize (None,480)
    fit "contain"

image sca01_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca01.png"))
    xysize (None,480)
    fit "contain"

image sca02_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca02.png"))
    xysize (None,480)
    fit "contain"

image sca03_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca03.png"))
    xysize (None,480)
    fit "contain"

image sca04_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca04.png"))
    xysize (None,480)
    fit "contain"

image sca05_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca05.png"))
    xysize (None,480)
    fit "contain"

image sca06_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca06.png"))
    xysize (None,480)
    fit "contain"

image sca07_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca07.png"))
    xysize (None,480)
    fit "contain"

image sca08_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca08.png"))
    xysize (None,480)
    fit "contain"

image sca09_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca09.png"))
    xysize (None,480)
    fit "contain"

image sca11_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca11.png"))
    xysize (None,480)
    fit "contain"

image sca15_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca15.png"))
    xysize (None,480)
    fit "contain"

image sca17_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca17.png"))
    xysize (None,480)
    fit "contain"

image sca19_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca19.png"))
    xysize (None,480)
    fit "contain"

image sca23_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca23.png"))
    xysize (None,480)
    fit "contain"

image sca27_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca27.png"))
    xysize (None,480)
    fit "contain"

image sca29_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca29.png"))
    xysize (None,480)
    fit "contain"

image sca33_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca33.png"))
    xysize (None,480)
    fit "contain"

image sca34_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca34.png"))
    xysize (None,480)
    fit "contain"

image sca35_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca35.png"))
    xysize (None,480)
    fit "contain"

image sca36_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca36.png"))
    xysize (None,480)
    fit "contain"

image sca38_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca38.png"))
    xysize (None,480)
    fit "contain"

image sca39_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca39.png"))
    xysize (None,480)
    fit "contain"

image sca40_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca40.png"))
    xysize (None,480)
    fit "contain"

image sca41_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca41.png"))
    xysize (None,480)
    fit "contain"

image sca44_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca44.png"))
    xysize (None,480)
    fit "contain"

image sca45_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca45.png"))
    xysize (None,480)
    fit "contain"

image sca46_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca46.png"))
    xysize (None,480)
    fit "contain"

image sca52_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca52.png"))
    xysize (None,480)
    fit "contain"

image sca53_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca53.png"))
    xysize (None,480)
    fit "contain"

image sca58_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca58.png"))
    xysize (None,480)
    fit "contain"

image sca60_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca60.png"))
    xysize (None,480)
    fit "contain"

image sca62_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca62.png"))
    xysize (None,480)
    fit "contain"

image sca65_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca65.png"))
    xysize (None,480)
    fit "contain"

image sca67_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca67.png"))
    xysize (None,480)
    fit "contain"

image sca68_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca68.png"))
    xysize (None,480)
    fit "contain"

image sca80_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca80.png"))
    xysize (None,480)
    fit "contain"

image sca81_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca81.png"))
    xysize (None,480)
    fit "contain"

image sca82_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca82.png"))
    xysize (None,480)
    fit "contain"

image sca83_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca83.png"))
    xysize (None,480)
    fit "contain"

image sca84_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca84.png"))
    xysize (None,480)
    fit "contain"

image sca85_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca85.png"))
    xysize (None,480)
    fit "contain"

image sca86_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca86.png"))
    xysize (None,480)
    fit "contain"

image sca88_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca88.png"))
    xysize (None,480)
    fit "contain"

image sca89_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca89.png"))
    xysize (None,480)
    fit "contain"

image sca91_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca91.png"))
    xysize (None,480)
    fit "contain"

image sca93_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca93.png"))
    xysize (None,480)
    fit "contain"

image sca94_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca94.png"))
    xysize (None,480)
    fit "contain"

image sca96_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca96.png"))
    xysize (None,480)
    fit "contain"

image sca97_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca97.png"))
    xysize (None,480)
    fit "contain"

image sca98_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sca98.png"))
    xysize (None,480)
    fit "contain"

image scb01_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb01.png"))
    xysize (None,480)
    fit "contain"

image scb02_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb02.png"))
    xysize (None,480)
    fit "contain"

image scb04_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb04.png"))
    xysize (None,480)
    fit "contain"

image scb05_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb05.png"))
    xysize (None,480)
    fit "contain"

image scb06_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb06.png"))
    xysize (None,480)
    fit "contain"

image scb07_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb07.png"))
    xysize (None,480)
    fit "contain"

image scb09_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb09.png"))
    xysize (None,480)
    fit "contain"

image scb15_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb15.png"))
    xysize (None,480)
    fit "contain"

image scb19_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb19.png"))
    xysize (None,480)
    fit "contain"

image scb23_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb23.png"))
    xysize (None,480)
    fit "contain"

image scb33_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb33.png"))
    xysize (None,480)
    fit "contain"

image scb34_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb34.png"))
    xysize (None,480)
    fit "contain"

image scb38_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb38.png"))
    xysize (None,480)
    fit "contain"

image scb39_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb39.png"))
    xysize (None,480)
    fit "contain"

image scb40_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb40.png"))
    xysize (None,480)
    fit "contain"

image scb41_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb41.png"))
    xysize (None,480)
    fit "contain"

image scb45_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb45.png"))
    xysize (None,480)
    fit "contain"

image scb46_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb46.png"))
    xysize (None,480)
    fit "contain"

image scb52_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb52.png"))
    xysize (None,480)
    fit "contain"

image scb58_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb58.png"))
    xysize (None,480)
    fit "contain"

image scb60_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb60.png"))
    xysize (None,480)
    fit "contain"

image scb62_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb62.png"))
    xysize (None,480)
    fit "contain"

image scb65_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb65.png"))
    xysize (None,480)
    fit "contain"

image scb68_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb68.png"))
    xysize (None,480)
    fit "contain"

image scb80_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb80.png"))
    xysize (None,480)
    fit "contain"

image scb81_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb81.png"))
    xysize (None,480)
    fit "contain"

image scb82_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb82.png"))
    xysize (None,480)
    fit "contain"

image scb83_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb83.png"))
    xysize (None,480)
    fit "contain"

image scb84_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb84.png"))
    xysize (None,480)
    fit "contain"

image scb85_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb85.png"))
    xysize (None,480)
    fit "contain"

image scb86_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb86.png"))
    xysize (None,480)
    fit "contain"

image scb88_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb88.png"))
    xysize (None,480)
    fit "contain"

image scb89_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb89.png"))
    xysize (None,480)
    fit "contain"

image scb91_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb91.png"))
    xysize (None,480)
    fit "contain"

image scb93_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb93.png"))
    xysize (None,480)
    fit "contain"

image scb96_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb96.png"))
    xysize (None,480)
    fit "contain"

image scb97_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scb97.png"))
    xysize (None,480)
    fit "contain"

image scc01_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc01.png"))
    xysize (None,480)
    fit "contain"

image scc02_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc02.png"))
    xysize (None,480)
    fit "contain"

image scc04_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc04.png"))
    xysize (None,480)
    fit "contain"

image scc07_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc07.png"))
    xysize (None,480)
    fit "contain"

image scc09_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc09.png"))
    xysize (None,480)
    fit "contain"

image scc15_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc15.png"))
    xysize (None,480)
    fit "contain"

image scc19_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc19.png"))
    xysize (None,480)
    fit "contain"

image scc38_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc38.png"))
    xysize (None,480)
    fit "contain"

image scc39_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc39.png"))
    xysize (None,480)
    fit "contain"

image scc40_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc40.png"))
    xysize (None,480)
    fit "contain"

image scc41_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc41.png"))
    xysize (None,480)
    fit "contain"

image scc45_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc45.png"))
    xysize (None,480)
    fit "contain"

image scc46_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc46.png"))
    xysize (None,480)
    fit "contain"

image scc58_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc58.png"))
    xysize (None,480)
    fit "contain"

image scc65_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc65.png"))
    xysize (None,480)
    fit "contain"

image scc68_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc68.png"))
    xysize (None,480)
    fit "contain"

image scc80_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc80.png"))
    xysize (None,480)
    fit "contain"

image scc81_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc81.png"))
    xysize (None,480)
    fit "contain"

image scc82_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc82.png"))
    xysize (None,480)
    fit "contain"

image scc83_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc83.png"))
    xysize (None,480)
    fit "contain"

image scc85_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc85.png"))
    xysize (None,480)
    fit "contain"

image scc86_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc86.png"))
    xysize (None,480)
    fit "contain"

image scc89_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc89.png"))
    xysize (None,480)
    fit "contain"

image scc91_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc91.png"))
    xysize (None,480)
    fit "contain"

image scc96_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc96.png"))
    xysize (None,480)
    fit "contain"

image scc97_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scc97.png"))
    xysize (None,480)
    fit "contain"

image scd01_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scd01.png"))
    xysize (None,480)
    fit "contain"

image scd02_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scd02.png"))
    xysize (None,480)
    fit "contain"

image scd04_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scd04.png"))
    xysize (None,480)
    fit "contain"

image scd07_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scd07.png"))
    xysize (None,480)
    fit "contain"

image scd09_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scd09.png"))
    xysize (None,480)
    fit "contain"

image scd15_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scd15.png"))
    xysize (None,480)
    fit "contain"

image scd39_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scd39.png"))
    xysize (None,480)
    fit "contain"

image scd40_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scd40.png"))
    xysize (None,480)
    fit "contain"

image scd41_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scd41.png"))
    xysize (None,480)
    fit "contain"

image scd45_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scd45.png"))
    xysize (None,480)
    fit "contain"

image scd46_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scd46.png"))
    xysize (None,480)
    fit "contain"

image scd58_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scd58.png"))
    xysize (None,480)
    fit "contain"

image scd65_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scd65.png"))
    xysize (None,480)
    fit "contain"

image scd68_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scd68.png"))
    xysize (None,480)
    fit "contain"

image scd81_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scd81.png"))
    xysize (None,480)
    fit "contain"

image scd82_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scd82.png"))
    xysize (None,480)
    fit "contain"

image scd83_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scd83.png"))
    xysize (None,480)
    fit "contain"

image scd85_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scd85.png"))
    xysize (None,480)
    fit "contain"

image scd86_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scd86.png"))
    xysize (None,480)
    fit "contain"

image scd89_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scd89.png"))
    xysize (None,480)
    fit "contain"

image sce07_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sce07.png"))
    xysize (None,480)
    fit "contain"

image sce09_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sce09.png"))
    xysize (None,480)
    fit "contain"

image sce15_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sce15.png"))
    xysize (None,480)
    fit "contain"

image sce40_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sce40.png"))
    xysize (None,480)
    fit "contain"

image sce45_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sce45.png"))
    xysize (None,480)
    fit "contain"

image sce46_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sce46.png"))
    xysize (None,480)
    fit "contain"

image sce58_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sce58.png"))
    xysize (None,480)
    fit "contain"

image sce65_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sce65.png"))
    xysize (None,480)
    fit "contain"

image sce68_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sce68.png"))
    xysize (None,480)
    fit "contain"

image sce82_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sce82.png"))
    xysize (None,480)
    fit "contain"

image sce85_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sce85.png"))
    xysize (None,480)
    fit "contain"

image sce86_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sce86.png"))
    xysize (None,480)
    fit "contain"

image scn00_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scn00.png"))
    xysize (None,480)
    fit "contain"

image scn01_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scn01.png"))
    xysize (None,480)
    fit "contain"

image scn02_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scn02.png"))
    xysize (None,480)
    fit "contain"

image scn06_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scn06.png"))
    xysize (None,480)
    fit "contain"

image scn07_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scn07.png"))
    xysize (None,480)
    fit "contain"

image scn10_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scn10.png"))
    xysize (None,480)
    fit "contain"

image sco00_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sco00.png"))
    xysize (None,480)
    fit "contain"

image sco02_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sco02.png"))
    xysize (None,480)
    fit "contain"

image sco06_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sco06.png"))
    xysize (None,480)
    fit "contain"

image sco07_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("sco07.png"))
    xysize (None,480)
    fit "contain"

image scp00_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scp00.png"))
    xysize (None,480)
    fit "contain"

image scp07_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scp07.png"))
    xysize (None,480)
    fit "contain"

image scq07_cutin:
    Crop((0,0,1914,1024), ReverseAlphaMask("scq07.png"))
    xysize (None,480)
    fit "contain"