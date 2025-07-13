label avg101504:

stop music
scene placeholderbackground
$ update_portrait('sc007_01 2', 'p15', [l(-17), light, flip], 6)
$ update_narrator('c151')
window show
with fade_in
c151 '[textdict[1221271]]'
$ update_portrait('sc007_01 2', 'p15', [l(-17), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1221272]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
c151 '[textdict[1221273]]'
menu:
    extend ""
    "[textdict[1221274]]":
        call avg101505
    "[textdict[1221275]]":
        call avg101506
    "[textdict[1221276]]":
        call avg101507
return