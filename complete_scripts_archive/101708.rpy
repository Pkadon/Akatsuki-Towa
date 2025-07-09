label avg101708:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1221894]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc009_01 1', 'p17', [l(-13), light, flip], 6)
c171 '[textdict[1221895]]'
$ update_portrait('sc009_01 1', 'p17', [l(-13), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1221896]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc009_01 5', 'p17', [l(-13), light, flip], 6)
c171 '[textdict[1221897]]'
menu:
    extend ""
    "[textdict[1221898]]":
        call avg101709
    "[textdict[1221899]]":
        call avg101710
    "[textdict[1221900]]":
        call avg101711
return