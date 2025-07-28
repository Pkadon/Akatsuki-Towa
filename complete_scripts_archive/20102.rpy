label avg20102:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1004995)]'
menu:
    extend ""
    "[textdict[1004996]]":
        call avg10063
    "[textdict[1004997]]":
        call avg10064
return