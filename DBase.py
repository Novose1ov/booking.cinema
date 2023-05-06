import pandas as pd
import os


class Table:
    def __init__(self, name:str) -> None:
        """Таблицы
        -
        ['films', 'holls', 'sessions', 'users']
        - 'films' : id, name, genre, time_film, description
        - 'holls' : id, name, row, col
        - 'sessions' : id, period, id_film, id_holl, date
        - 'users' : id, log, password
 

        Args:
            name (str): Название таблицы, с которой мы хотим работать

        """
        if name not in ['films', 'holls', 'sessions', 'users']:
            raise ValueError ('DataBaseError. Not found name of table.')
        self.name = name
        

    def astypeTable(self) -> None:
        """Функция для правильной типизации данных
        """
        if self.name == 'films':
            # id, name, genre, time_film, description
            self.table['id'] = self.table['id'].astype(int)
            self.table['name'] = self.table['name'].astype(str)
            self.table['genre'] = self.table['genre'].astype(str)
            self.table['time_film'] = self.table['time_film'].astype(str)
            self.table['description'] = self.table['description'].astype(str)
        elif self.name == 'holls':
            # id, name, row, col
            self.table['id'] = self.table['id'].astype(int)
            self.table['name'] = self.table['name'].astype(str)
            self.table['row'] = self.table['row'].astype(int)
            self.table['col'] = self.table['col'].astype(int)
        elif self.name == 'sessions':
            # id, period, id_film, id_holl, date
            self.table['id'] = self.table['id'].astype(int)
            self.table['period'] = self.table['period'].astype(int)
            self.table['id_film'] = self.table['id_film'].astype(int)
            self.table['id_holl'] = self.table['id_holl'].astype(int)
            self.table['date'] = self.table['date'].astype(str)
        elif self.name == 'users':
            # id, log, password
            self.table['id'] = self.table['id'].astype(int)
            self.table['log'] = self.table['log'].astype(str)
            self.table['password'] = self.table['password'].astype(str)        
        
        
    def append(self, data:list=[]) -> None:
        """Добавляет элементы в конец таблицы.
        -
        Args:
            data (list): Список элементов в порядке столбцов в таблице.
            
            Количество колонок каждой таблице:
            - films = 5
            - holls = 4
            - sessions = 5
            - users = 3
        """
        if data is None:
            return None
        
        self.table = pd.read_csv(os.path.abspath(f'{self.name}.csv'), sep=',')
        if len(data) == self.table.shape[1]:
            self.table.loc[self.table.shape[0]+1, :] = data
            self.astypeTable()
            self.table = self.table.sort_values(by='id')
            self.table.to_csv(os.path.abspath(f'{self.name}.csv'), index=False)
        else:
            raise ValueError ('DataBaseError. The number of elements does not correspond to the columns.')
    
    
    def drop(self, name:str) -> None:
        """Удаляет полностью строку по name.
        """
        self.table = pd.read_csv(os.path.abspath(f'{self.name}.csv'), sep=',')
        self.table.drop(self.table[self.table['name'] == name].index, axis=0, inplace=True)
        self.table.to_csv(os.path.abspath(f'{self.name}.csv'), index=False)
        
        
    def get_element(self, id:int, coulumn:int) -> str:
        """Получает ячейку по id и номеру колонки, начиная с 0.
        """
        try:
            self.table = pd.read_csv(os.path.abspath(f'{self.name}.csv'), sep=',')
            mask = self.table[self.table['id'] == id].index[0]
            return self.table.iloc[mask, coulumn]
        except IndexError:
            print('Ячейка не найдена')
        
        
    def set_element(self, id:int, coulumn:int, data) -> None:
        """Изменяет ячейку на значение data по id и номеру колонки, начиная с 0.
        """
        try:
            self.table = pd.read_csv(os.path.abspath(f'{self.name}.csv'), sep=',')
            mask = self.table[self.table['id'] == id].index[0]
            self.table.iloc[mask, coulumn] = data
            self.table.to_csv(os.path.abspath(f'{self.name}.csv'), index=False)
        except IndexError:
            print('Ячейка не найдена')
            
    
    def get_collection_by_dates(self, date:str) -> list[list]:
        """По дате возврашает все сеансы из таблицы 'sessions'
        """
        if self.name == 'sessions':
            self.table = pd.read_csv(os.path.abspath(f'{self.name}.csv'), sep=',')
            t_date = self.table[self.table['date'] == date]
            result = []
            for i in range(t_date.shape[0]):
                result.append(list(t_date.iloc[i, :]))
            return result
        
        
    def get_collection_by_index(self) -> list[list]:
        """По дате возврашает все сеансы из таблицы 'sessions'
        """
        self.table = pd.read_csv(os.path.abspath(f'{self.name}.csv'), sep=',')
        result = []
        for i in range(self.table.shape[0]):
            result.append(list(self.table.iloc[i, :]))
        return result
    
    
    def clear(self):
        self.table = pd.read_csv(os.path.abspath(f'{self.name}.csv'), sep=',')
        self.table.drop(self.table.index, inplace=True)
        self.table.to_csv(os.path.abspath(f'{self.name}.csv'), index=False)
        
        
    def is_row_in_table(self, data):
        self.table = pd.read_csv(os.path.abspath(f'{self.name}.csv'), sep=',')
        if self.name != 'users':
            if list(self.table['name']) == []:
                return False
            return True if (self.table['name'] == data[1]).max() else False
        else:
            if list(self.table['log']) == []:
                return False
            return True if (self.table['log'] == data[1]).max() else False
        
        
        
if __name__ == '__main__':
    pass