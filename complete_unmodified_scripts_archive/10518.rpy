label avg10518:

$ play_music("ED6100.ogg")
scene avg_bg_023
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1151817)]' (**arg(1, 1151817))
play sfx2 "other_7047.ogg"
get_char('c0') '[convertstrid(1151818)]' (**arg(2, 1151818))
$ update_portrait('st040_01 1', 'p239', [l_entrance(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1151819)]' (**arg(3, 1151819))
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1151820)]' (**arg(4, 1151820))
hide p239
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c12021') '[convertstrid(1151821)]' (**arg(5, 1151821))
hide p1
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1151822)]' (**arg(6, 1151822))
hide p3
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1151823)]' (**arg(7, 1151823))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li07.ogg"
get_char('c41') '[convertstrid(1151824)]' (**arg(8, 1151824))
hide p4
$ update_portrait('st040_01 2', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1151825)]' (**arg(9, 1151825))
hide p2
$ update_portrait('st040_01 2', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1151826)]' (**arg(10, 1151826))
hide p239
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1151827)]' (**arg(11, 1151827))
hide p3
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1151828)]' (**arg(12, 1151828))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li17.ogg"
get_char('c41') '[convertstrid(1151829)]' (**arg(13, 1151829))
hide p4
hide p2
$ update_narrator('c13')
with fade
$ update_portrait('oc001_01 10', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1151830)]' (**arg(14, 1151830))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c12021') '[convertstrid(1151831)]' (**arg(15, 1151831))
get_char('c12021') '[convertstrid(1151832)]' (**arg(16, 1151832))
$ update_portrait('oc003_01 2', 'p3', [l_entrance(-6), light, flip], 6)
get_char('c31') '[convertstrid(1151833)]' (**arg(17, 1151833))
hide p1
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1151834)]' (**arg(18, 1151834))
hide p3
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
get_char('c12021') '[convertstrid(1151835)]' (**arg(19, 1151835))
$ update_portrait('st040_01 1', 'p239', [l_entrance(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1151836)]' (**arg(20, 1151836))
hide p4
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1151837)]' (**arg(21, 1151837))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1151838)]' (**arg(22, 1151838))
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1151839)]' (**arg(23, 1151839))
hide p2
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151840)]' (**arg(24, 1151840))
hide p239
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c12021') '[convertstrid(1151841)]' (**arg(25, 1151841))
get_char('c12021') '[convertstrid(1151842)]' (**arg(26, 1151842))
$ update_portrait('oc003_01 4', 'p3', [l_entrance(-6), light, flip], 6)
get_char('c31') '[convertstrid(1151843)]' (**arg(27, 1151843))
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1151844)]' (**arg(28, 1151844))
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1151845)]' (**arg(29, 1151845))
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1151846)]' (**arg(30, 1151846))
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro10.ogg"
get_char('c31') '[convertstrid(1151847)]' (**arg(31, 1151847))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1151848)]' (**arg(32, 1151848))
hide p3
hide p4
$ update_narrator('c23')
with fade
$ update_portrait('oc002_01 2', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1151849)]' (**arg(33, 1151849))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1151850)]' (**arg(34, 1151850))
hide p2
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151851)]' (**arg(35, 1151851))
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1151852)]' (**arg(36, 1151852))
hide p1
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc003_01 7', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1151853)]' (**arg(37, 1151853))
hide p3
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1151854)]' (**arg(38, 1151854))
hide p239
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c12021') '[convertstrid(1151855)]' (**arg(39, 1151855))
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1151856)]' (**arg(40, 1151856))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
get_char('c12021') '[convertstrid(1151857)]' (**arg(41, 1151857))
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1151858)]' (**arg(42, 1151858))
return