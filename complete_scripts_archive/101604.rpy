label avg101604:

stop music
scene placeholderbackground
$ update_portrait('sc008_01 2', 'p16', [l(-18), light, flip], 6)
$ update_narrator('c161')
window show
with fade_in
c161 '[convertstrid(1221539)]'
$ update_portrait('sc008_01 2', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1221540)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[convertstrid(1221541)]'
menu:
    extend ""
    "[textdict[1221542]]":
        call avg101605
    "[textdict[1221543]]":
        call avg101606
    "[textdict[1221547]]":
        call avg101607
return