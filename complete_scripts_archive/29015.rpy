label avg29015:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1007253)]'
menu:
    extend ""
    "[textdict[1007254]]":
        call avg29016
    "[textdict[1007255]]":
        call avg29017
return