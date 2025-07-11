label avg101804:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1222166]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc010_01 1', 'p18', [l(-10), light, flip], 6)
c181 '[textdict[1222167]]'
$ update_portrait('sc010_01 4', 'p18', [l(-10), light, flip], 6)
c181 '[textdict[1222168]]'
menu:
    extend ""
    "[textdict[1222169]]":
        call avg101805
    "[textdict[1222170]]":
        call avg101806
    "[textdict[1222171]]":
        call avg101807
return