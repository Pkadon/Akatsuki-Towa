label avg103021:
stop music

scene placeholderbackground
$ update_portrait('sc022_01 4', 'p30', [l(-9), light, flip], 6)
window show
with fade_in
c301 '[textdict[1222471]]'
$ update_portrait('sc022_01 4', 'p30', [l(-9), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1222472]]'
hide p30
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc022_01 1', 'p30', [l(-9), light, flip], 6)
c301 '[textdict[1222473]]'
hide p1
$ update_portrait('sc022_01 1', 'p30', [l(-9), dark, flip], 6)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 5)
c13 '[textdict[1222474]]'
hide p30
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc022_01 5', 'p30', [l(-9), light, flip], 6)
c301 '[textdict[1222475]]'
hide p30
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc022_01 1', 'p30', [l(-9), light, flip], 6)
c301 '[textdict[1222476]]'
menu:
    extend ""
    "[textdict[1222477]]":
        call avg103022
    "[textdict[1222478]]":
        call avg103023
    "[textdict[1222479]]":
        call avg103024
return