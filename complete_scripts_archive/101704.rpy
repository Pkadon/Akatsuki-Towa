label avg101704:

stop music
scene placeholderbackground
$ update_portrait('sc009_01 1', 'p17', [l(-13), light, flip], 6)
$ update_narrator('c171')
window show
with fade_in
c171 '[convertstrid(1221883)]'
$ update_portrait('sc009_01 1', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1221884)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc009_01 1', 'p17', [l(-13), light, flip], 6)
c171 '[convertstrid(1221885)]'
$ update_portrait('sc009_01 1', 'p17', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1221886)]'
menu:
    extend ""
    "[textdict[1221887]]":
        call avg101705
    "[textdict[1221888]]":
        call avg101706
    "[textdict[1221889]]":
        call avg101707
return