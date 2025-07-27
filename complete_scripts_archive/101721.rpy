label avg101721:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1221932)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc009_01 1', 'p17', [l(-13), light, flip], 6)
c171 '[convertstrid(1221933)]'
$ update_portrait('sc009_01 1', 'p17', [l(-13), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1221934)]'
menu:
    extend ""
    "[textdict[1221935]]":
        call avg101722
    "[textdict[1221936]]":
        call avg101723
    "[textdict[1221937]]":
        call avg101724
return