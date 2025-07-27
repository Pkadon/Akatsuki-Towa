label avg29042:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1100027)]'
menu:
    extend ""
    "[textdict[1100028]]":
        call avg29043
    "[textdict[1100029]]":
        call avg29044
return