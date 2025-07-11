label avg25064:

scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
window show
with fade_in
c23 '[textdict[1210190]]'
hide p2
$ update_portrait('oc001_01 17', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210191]]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
c23 '[textdict[1210192]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210193]]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
c23 '[textdict[1210194]]'
menu:
    extend ""
    "[textdict[1210238]]":
        call avg25065
    "[textdict[1210239]]":
        call avg25066
return