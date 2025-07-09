label avg101821:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1222215]]'
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('sc010_01 4', 'p18', [l(-10), light, flip], 6)
c181 '[textdict[1222216]]'
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('sc010_01 1', 'p18', [l(-10), light, flip], 6)
c181 '[textdict[1222217]]'
menu:
    extend ""
    "[textdict[1222218]]":
        call avg101822
    "[textdict[1222219]]":
        call avg101823
    "[textdict[1222220]]":
        call avg101824
return