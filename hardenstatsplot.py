from sportsreference.nba.roster import Player
import matplotlib.pyplot as plt
import numpy as np
##from matplotlib.backends.backend_pdf import PdfPages

##pdf = PdfPages('multipage.pdf')
##fig1 = plt.figure()

jharden = Player('hardeja01')

points0708 = jharden('2007-08').points
points0809 = jharden('2008-09').points
points0910 = jharden('2009-10').points
points1011 = jharden('2010-11').points
points1112 = jharden('2011-12').points
points1213 = jharden('2012-13').points
points1314 = jharden('2013-14').points
points1415 = jharden('2014-15').points
points1516 = jharden('2015-16').points
points1617 = jharden('2016-17').points
points1718 = jharden('2017-18').points


turnovers0708 = jharden('2007-08').turnovers
turnovers0809 = jharden('2008-09').turnovers
turnovers0910 = jharden('2009-10').turnovers
turnovers1011 = jharden('2010-11').turnovers
turnovers112 = jharden('2011-12').turnovers
turnovers1213 = jharden('2012-13').turnovers
turnovers1314 = jharden('2013-14').turnovers
turnovers1415 = jharden('2014-15').turnovers
turnovers1516 = jharden('2014-15').turnovers
turnovers1617 = jharden('2014-15').turnovers
turnovers1718 = jharden('2014-15').turnovers

plt.title('James Harden Points vs Turnovers')
#plt.ylabel('Total Points Scored')
#plt.xlabel('Turnovers')
##plt.legend(loc = 'best')
plt.ylabel('Turnovers')
plt.xlabel('Points')
plt.axis([1000,2500, 50, 500])
plt.scatter([points0708,points0809,points0910,points1011,points1112,points1213,points1314,points1415, points1516, points1617, points1718], 
[turnovers0708, turnovers0809, turnovers0910, turnovers1011, turnovers112, turnovers1213, turnovers1314, turnovers1415, turnovers1516, turnovers1617, turnovers1718] ) 
##plt.plot(, label = 'Turnovers')
#plt.xticks([season1415, season1516, season1617, season1718])
plt.show()



