# from collections import Counter
class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})
        
    def total_visits(self):
        return len(self.trips()) if len(self.trips()) else 0
    
    def best_visitor(self):

        # GITHUB ATTEMPTS      
        visitors = [trip.visitor for trip in self.trips()]

        # VERSION 1
        # counts = {visitor: visitors.count(visitor) for visitor in visitors}
        # sorted_list = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
        # return sorted_list[0][0]

        # VERSION 2
        # return Counter(visitors).most_common(1)[0][0]

        # VERSION 3
        return max(set(visitors), key=visitors.count)
    

        # NICK ATTEMPTS
    
        # # FUNCTIONALITY WORKS BUT DOESN'T PASS TEST
        # visits = [trip.visitor for trip in self.trips() if trip.national_park == self]
        # # print(visits)
        # most_visitor = max(visits, key= visits.count)

        # METHOD ATTEMPT
        # print(visits.sort(key=visits.count, reverse=True))
        # l= Counter(visits).most_common(1)[0][0]
        # print(l)
     
        # METHOD 2 ATTEMPT
        # print(most_visitor)
        # sorted_visits =  visits.sort(reverse = True)
        # print(sorted_visits)
        # return sorted_visits[1]


    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and not hasattr(self, "name") and 3 <= len(value):
            self._name = value

    @classmethod
    def most_visited(cls):
        return max(cls.all, key=lambda park: park.total_visits())

class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self, value):
        if isinstance(value, str) and 7 <= len(value):
            self._start_date = value

    @property
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self, value):
        if isinstance(value, str) and 7 <= len(value):
            self._end_date = value

    @property 
    def visitor(self):
        return self._visitor
    @visitor.setter
    def visitor(self, value):
        if isinstance(value, Visitor):
            self._visitor = value

    @property
    def national_park(self):
        return self._national_park
    @national_park.setter
    def national_park(self, value):
        if isinstance(value, NationalPark):
            self._national_park = value


class Visitor:

    all = []

    def __init__(self, name):
        self.name = name
        Visitor.all.append(self)
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})
        
    
    def total_visits_at_park(self, park):
        return len(self.national_parks()) if len(self.national_parks()) else 0
    

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <=15:
            self._name = value

    
el_dorado = NationalPark("El Dorado")
nick = Visitor("Nick")
stephen= Visitor("Stephen")
vacation = Trip(visitor=nick,national_park= el_dorado, start_date="May 5th",end_date= "May 9th")
vacation2 = Trip(visitor=nick,national_park= el_dorado, start_date="May 5th",end_date= "May 9th")
vacation3 = Trip(visitor=nick,national_park= el_dorado, start_date="May 5th",end_date= "May 9th")
el_dorado.best_visitor()



