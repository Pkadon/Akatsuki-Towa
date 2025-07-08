label avg24085:
stop music

play music "ed7105.ogg"
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
window show
with fade_in
c11 '[textdict[1200314]]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('st044_01 1', 'p243', [r(10), light], 5)
c2433 '[textdict[1200315]]'
hide p1
$ update_portrait('st044_01 1', 'p243', [r(10), dark], 5)
$ update_portrait('oc001_01 11', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1200316]]'
return