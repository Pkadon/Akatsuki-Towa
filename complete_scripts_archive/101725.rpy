label avg101725:

stop music
scene placeholderbackground
$ update_portrait('sc009_01 4', 'p17', [l(-13), light, flip], 6)
$ update_narrator('c171')
window show
with fade_in
c171 '[convertstrid(1221942)]'
$ update_portrait('sc009_01 4', 'p17', [l(-13), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1221943)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1221944)]'
menu:
    extend ""
    "[textdict[1221945]]":
        call avg101726
    "[textdict[1221946]]":
        call avg101727
    "[textdict[1221947]]":
        call avg101728
return