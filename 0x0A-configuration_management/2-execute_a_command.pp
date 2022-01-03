# Manifest that kills a provcess named killmenow
exec {'killer':
	command => '/bin/pkill killmenow',
}
