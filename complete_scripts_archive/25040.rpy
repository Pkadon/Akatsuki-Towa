label avg25040:

scene placeholderbackground
$ update_portrait('uc001_02 3', 'p2001', [mid(6), light], 5)
window show
with fade_in
c20013 '[textdict[1210102]]'
hide p2001
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210103]]'
hide p1
$ update_portrait('uc001_02 2', 'p2001', [mid(6), light], 5)
c20013 '[textdict[1210104]]'
menu:
    extend ""
    "[textdict[1214999]]":
        call avg25041
    "[textdict[1215000]]":
        call avg25000
return