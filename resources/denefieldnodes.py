denefield = {'Reception':{'ReceptionE':12},
			'ReceptionE':{'Reception':12, 'CanteenE1':18, 'Canteen1':18, 'Outside1':41},
			'CanteenE1':{'ReceptionE':18, 'Centeen1':6},
			'Canteen1':{'ReceptionE':18, 'CanteenE1':6, 'Centeen2':33},
			'Canteen2':{'Canteen1':33, 'Canteen3':5},
			'Canteen3':{'Canteen2':5, 'Canteen4':22},
			'Centeen4':{'Canteen3':22, 'Canteen5':23},
			'Canteen5':{'Canteen4':23, 'CanteenE2':30},
			'CanteenE2':{'Canteen5':30, 'Halls':22},
			'Halls':{'CanteenE2':22, 'Pe':15},
			'Pe':{'Halls':15, 'PeE':15},
			'PeE':{'Pe':15, 'Hum1':20},
			'Hum1':{'PeE':20, 'HumE1':20, 'HumE2':25},
			'HumE1':{'Hum1':20, 'Hum2':6},
			'Hum2':{'HumE1':6, 'Hum3':7},
			'Hum3':{'Hum2':7, 'Hum4':11},
			'Hum4':{'Hum3':11, 'HumE2':11, 'Hum5':10},
			'HumE2':{'Hum1':25, 'Hum4':11, 'SReception':8, 'TechE':20},
			'SReception':{'HumE2':8},
			'Hum5':{'Hum4':10, 'Library':8},
			'Library':{'Hum5':8, 'TechE':15, 'Y11CR':17},
			'TechE':{'HumE2':20, 'Library':15, 'Tech1':18, 'Math5':27},
			'Y11CR':{'Library':17, 'SciE1':46},
			'SciE1':{'Y11CR':46, 'Sci1':20},
			'Sci1':{'SciE1':20, 'Tech3':22, 'SciS1':7, 'DV1':11},
			'Tech3':{'Sci1':22, 'Drama1':25, 'Tech2':25},
			'Tech2':{'Tech3':25, 'Tech1':6},
			'Tech1':{'Tech2':6, 'TechE':18},
			'SciS1':{'Sci1':7, 'DV1':7},
			'DV1':{'Sci1':11, 'SciS1':7, 'DV2':14, 'DV5':11},
			'DV2':{'DV1':14, 'DV3':11},
			'DV3':{'DV2':11, 'DV5':15, 'DV4':15, 'Drama1':13},
			'Drama1':{'DV3':13, 'Art1':18, 'Tech3':25},
			'Art1':{'Drama1': 18},
			'DV5':{'DV1':11, 'DV3':15, 'DV6':15},
			'DV4':{'DV3':15, 'DV6':16},
			'DV6':{'DV5':15, 'DV4':16},
			'Drama2':{'DV6':7, 'Sci2':24},
			'Sci2':{'Drama2':24, 'Music1':25, 'SciS2':14, 'SciE2':14},
			'Music1':{'Sci2':25, 'Music2':25},
			'Music2':{'Music1':25, 'Arts':13},
			'Arts':{'Music2':13}
