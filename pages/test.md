Title: Test
Published: 22 Dec 2016
Description: 
Tags: 

Of course, you don't have to set the width to 50%. Any width less than the containing div will work. The margin: 0 auto is what does the actual centering.

If you are targeting IE8+, it might be better to have this instead:

	#inner {
		display: table;
		margin: 0 auto;
	}

It will make the inner element center horizontally and it works without setting a specific width.

Working example here:

	#inner {
		display: table;
		margin: 0 auto; 
	}