label avg24095:
stop music

play music "ed7105.ogg"
scene placeholderbackground
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
window show
with fade_in
c21 '[textdict[1200337]]'
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 6)
c50133 '[textdict[1200338]]'
hide p2
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1200339]]'
return