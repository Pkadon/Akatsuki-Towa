label avg29018:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1007258)]'
menu:
    extend ""
    "[textdict[1007254]]":
        call avg29019
    "[textdict[1007255]]":
        call avg29017
return