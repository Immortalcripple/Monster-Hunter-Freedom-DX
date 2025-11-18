HallSelectWHook			equ 0x08838864
SaveDataOffset			equ 0x09858C20
HallSelectOffset		equ 0x0985929B

	HallSelectW:
		li			a3, 0x0
		xori		v1, v1, 0x1
		la			t0, SaveDataOffset
		sb			v1, 0x4F(t0)
		la			t0, HallSelectWHook
		addi		t0, t0, 0x8
		jr			t0
		nop
		
	HallSelectR:
		la			a0, SaveDataOffset
		lb			t0, 0x4F(a0)
		la			a0, HallSelectOffset
		sb			t0, 0x0(a0)
		jr			ra
		nop
		
	.org HallSelectWHook
		j			HallSelectW
		nop