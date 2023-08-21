class workout:
    def __init__(self,date: str,day: str ,workout: str ,sets: list) -> dict:
        self.date = date
        self.day = day
        self.workout = workout
        self.sets = sets

    def add_set(self ,reps: int , weight: int):
        
        latest_set=int(self.sets[-1][-1])
        self.sets.append("set"+str(latest_set+1))
    

    def export(self):
        return {"date":self.date, "day":self.day,"workout":self.workout,"set":self.sets}




