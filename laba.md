```cpp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lab_3_cherepnin
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Создание экземпляра класса для работы с коллекцией компонентов
            Collection_components collection_components = new Collection_components();

            Console.WriteLine("=== ТЕСТИРОВАНИЕ ПРОГРАММЫ ===\n");

            // 1. Тест начального заполнения коллекции
            Console.WriteLine("1. ТЕСТ НАЧАЛЬНОГО ЗАПОЛНЕНИЯ КОЛЛЕКЦИИ:");
            collection_components.Filling_Collection();
            collection_components.Print_arr_components();
            collection_components.Print_arr_components_TTX();

            // 2. Тест вывода отдельных элементов
            Console.WriteLine("\n2. ТЕСТ ВЫВОДА ОТДЕЛЬНЫХ ЭЛЕМЕНТОВ:");
            Console.WriteLine("Через индексатор [1]:");
            collection_components[1].Print_One_component();

            Console.WriteLine("Через метод Print_One_Item_from_Collection(1):");
            collection_components.Print_One_Item_from_Collection(1);

            Console.WriteLine("Попытка вывода несуществующего элемента (индекс 11):");
            collection_components.Print_One_Item_from_Collection(11);

            // 3. Тест изменения элемента коллекции
            Console.WriteLine("\n3. ТЕСТ ИЗМЕНЕНИЯ ЭЛЕМЕНТА КОЛЛЕКЦИИ:");
            Console.WriteLine("До изменения:");
            collection_components.Print_One_Item_from_Collection(1);

            collection_components.Change_Item(1, new Order_Manager("Order manage Sber2", "C++", ProductType.frontend_component, "4.4.4", 777));

            Console.WriteLine("После изменения:");
            collection_components.Print_One_Item_from_Collection(1);

            // 4. Тест поиска по имени
            Console.WriteLine("\n4. ТЕСТ ПОИСКА ПО ИМЕНИ:");
            int foundIndex = collection_components.Find_compone_name("Order manage Sber2");
            Console.WriteLine($"Найденный индекс: {foundIndex}");

            // Поиск несуществующего элемента
            int notFoundIndex = collection_components.Find_compone_name("Несуществующий компонент");
            Console.WriteLine($"Поиск несуществующего элемента: {notFoundIndex}");

            // 5. Тест работы с разными типами компонентов
            Console.WriteLine("\n5. ТЕСТ РАБОТЫ С РАЗНЫМИ ТИПАМИ КОМПОНЕНТОВ:");
            Console.WriteLine("Создание и вывод серверного компонента:");
            Srv_Restrictions srvTest = new Srv_Restrictions("Test Server", "Java", ProductType.server_component, "2.0.0", 1200);
            srvTest.Print_One_component();
            srvTest.Database();

            Console.WriteLine("\nСоздание и вывод фронтенд компонента:");
            Order_Manager frontTest = new Order_Manager("Test Frontend", "JavaScript", ProductType.frontend_component, "3.1.0", 450);
            frontTest.Print_One_component();
            frontTest.Database();

            // 6. Тест валидации данных
            Console.WriteLine("\n6. ТЕСТ ВАЛИДАЦИИ ДАННЫХ:");
            Console.WriteLine("Попытка создания компонента с некорректным количеством строк кода:");
            Order_Manager invalidComponent = new Order_Manager("Invalid Component", "Python", ProductType.frontend_component, "1.0.0", 10); // Меньше минимального
            invalidComponent.Print_One_component();

            // 7. Тест граничных случаев
            Console.WriteLine("\n7. ТЕСТ ГРАНИЧНЫХ СЛУЧАЕВ:");
            Console.WriteLine("Обращение к индексатору с отрицательным индексом:");
            Component negativeIndex = collection_components[-1];
            Console.WriteLine($"Результат: {(negativeIndex == null ? "null" : negativeIndex.ToString())}");

            Console.WriteLine("Обращение к индексатору с индексом больше размера коллекции:");
            Component largeIndex = collection_components[100];
            Console.WriteLine($"Результат: {largeIndex}");

            // 8. Тест статических методов и свойств
            Console.WriteLine("\n8. ТЕСТ СТАТИЧЕСКИХ МЕТОДОВ И СВОЙСТВ:");
            Console.WriteLine($"Общее количество созданных компонентов: {Component.Count_component}");
            Component.Print_Line();

            // 9. Тест добавления компонентов по умолчанию
            Console.WriteLine("\n9. ТЕСТ ДОБАВЛЕНИЯ КОМПОНЕНТОВ ПО УМОЛЧАНИЮ:");
            // Раскомментируйте для тестирования:
            collection_components.Add_components();
            collection_components.Print_arr_components();

            // 10. Тест добавления компонентов с параметрами
            Console.WriteLine("\n10. ТЕСТ ДОБАВЛЕНИЯ КОМПОНЕНТОВ С ПАРАМЕТРАМИ:");
            // Раскомментируйте для тестирования:
            collection_components.Add_component_with_Parameters();
            collection_components.Print_arr_components();

            // 11. ТЕСТ ПОЛНОГО ЦИКЛА СЕРИАЛИЗАЦИИ И ДЕСЕРИАЛИЗАЦИИ
            Console.WriteLine("\n11. ТЕСТ ПОЛНОГО ЦИКЛА СЕРИАЛИЗАЦИИ И ДЕСЕРИАЛИЗАЦИИ:");
            Console.WriteLine("=== НАЧАЛО ТЕСТА СОХРАНЕНИЯ/ЗАГРУЗКИ ===");

            // Сохраняем текущую коллекцию в файл
            Console.WriteLine("\nШАГ 1: Сохранение коллекции в XML файл...");
            collection_components.Serialize_Collection_Component();
            Console.WriteLine("Коллекция успешно сохранена в файл 'save_arr_components.xml'");

            // Показываем текущее состояние
            Console.WriteLine("\nШАГ 2: Текущее состояние коллекции (перед очисткой):");
            collection_components.Print_arr_components();
            Console.WriteLine($"Количество компонентов до очистки: {Component.Count_component}");

            // Очищаем коллекцию
            Console.WriteLine("\nШАГ 3: Полная очистка коллекции...");
            collection_components.Clearing_Collection();
            Console.WriteLine("Коллекция очищена");

            // Показываем пустую коллекцию
            Console.WriteLine("\nШАГ 4: Состояние после очистки:");
            collection_components.Print_arr_components();
            Console.WriteLine($"Количество компонентов после очистки: {Component.Count_component}");

            // Восстанавливаем коллекцию из файла
            Console.WriteLine("\nШАГ 5: Загрузка коллекции из XML файла...");
            collection_components.DeSerialize_Collection_Component();
            Console.WriteLine("Коллекция успешно загружена из файла");

            // Показываем восстановленную коллекцию
            Console.WriteLine("\nШАГ 6: Состояние после загрузки:");
            collection_components.Print_arr_components();
            Console.WriteLine($"Количество компонентов после загрузки: {Component.Count_component}");

            Console.WriteLine("=== ТЕСТ СОХРАНЕНИЯ/ЗАГРУЗКИ ЗАВЕРШЕН ===");

            // 12. Дополнительная проверка - тестируем поиск в восстановленной коллекции
            Console.WriteLine("\n12. ПРОВЕРКА ВОССТАНОВЛЕННОЙ КОЛЛЕКЦИИ:");
            Console.WriteLine("Поиск компонента 'Order manage Sber' в восстановленной коллекции:");
            int restoredIndex = collection_components.Find_compone_name("Order manage Sber");
            if (restoredIndex != -1)
            {
                Console.WriteLine($"Компонент найден на позиции {restoredIndex}");
                Console.WriteLine("Информация о найденном компоненте:");
                collection_components.Print_One_Item_from_Collection(restoredIndex);
            }
            else
            {
                Console.WriteLine("Компонент не найден в восстановленной коллекции");
            }

            // 13. Дополнительный тест - создание компонента с недопустимым типом
            Console.WriteLine("\n13. ТЕСТ С НЕДОПУСТИМЫМ ТИПОМ КОМПОНЕНТА:");
            Order_Manager wrongTypeComponent = new Order_Manager();
            wrongTypeComponent.Prod_type = ProductType.server_component; // Попытка установить серверный тип для фронтенд-компонента
            wrongTypeComponent.Print_One_component();

            Console.WriteLine("\n=== ВСЕ ТЕСТЫ ЗАВЕРШЕНЫ ===");
            Console.WriteLine("\nНажмите любую клавишу для выхода...");
            Console.ReadKey();
        }
    }
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace lab_3_cherepnin
{


    // Перечисление: Типы продуктов
    public enum ProductType
    {
        frontend_component,    // фронтенд-компонент
        server_component,      // серверный компонент  
        finished_product,      // готовый продукт
        unknown_type           // неизвестный тип
    }

    // Интерфейс для изделий
    interface I_izdelie
    {

        //Свойство для названия продукта (Реализовали в классе компонента)
        string Name { get; set;}

        // Свойство для версии продукта (Реализовали в классе компонента)
        string Version { get; set;}


        // Метод для указания используемой базы данных
        void Database();







    }
}
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Serialization;

namespace lab_3_cherepnin
{
    [Serializable]
    [XmlInclude(typeof(Srv_Restrictions))]
    [XmlInclude(typeof(Order_Manager))]
    public abstract class Component : I_izdelie
    {
        // Статическая часть
        // Поля ---------------------------------------------------------------------------

        // Статическое поле для подсчета количества компонент
        static int count_component = 0;

        // Методы -------------------------------------------------------------------------

        //Метод для увеличения счетчика компонент
        private static void Increment_component()
        {
            count_component++;
        }

        // Метод для уменьшения счетчика компонент
        public static void Decrement_component()
        {
            count_component--;
        }

        // Метод для вывода общего количества компонент
        public static void Print_count_component()
        {
            Console.WriteLine(count_component);
        }

        // Свойство для доступа к count_component
        public static int Count_component
        {
            get => count_component;
        }

        // ========================================================================================
        // Объектная часть
        // Поля ---------------------------------------------------------------------------
        // Поля класса
        string name;           // название компоненты
        string version;        // версия компоненты
        protected ProductType prod_type; // тип компоненты

        // Свойства ----------------------------------------------------------------------
        //Свойство для типа компаненты
        public virtual ProductType Prod_type
        {
            get => prod_type;
            set
            {
                // Проверка, что тип компаненты является допустимым
                if ((value & (ProductType.frontend_component | ProductType.server_component | ProductType.finished_product)) != 0)
                    prod_type = value;
                else
                    prod_type = ProductType.unknown_type;
            }
        }
        // Свойство для версии компаненты (реализация интерфейса I_izdelie)

        public string Version
        {
            get => version;
            set => version = value;
        }


        //Свойство для названия компаненты (реализация интерфейса I_izdelie)

        public string Name
        {
            get => name;
            set => name = value;
        }

        //Автоматическое свойство для языка программирования

        public string Programming_language { get; set; }


        // конструкторы ----------------------------------------------------------------

        //Конструктор по умолчанию

        public Component()
        {
            this.name = "неизвестное изделие";
            prod_type = ProductType.unknown_type;
            version = "0.0.0";
            Programming_language = "C#";
            Increment_component();// Увеличиваем счетчик компонентов
        }


        // Параметризованный конструктор


        public Component(string name, string prog_lang, ProductType prod, string vers)
        {
            this.name = name;
            prod_type = prod;
            this.version = vers;
            Programming_language = prog_lang;
            Increment_component(); // Увеличиваем счетчик компонентов
        }
        // Методы ------------------------------------------------------------------

        // Переопределение метода ToString()
        // Создает строку, описывающюю объект данного класса
        //Переопределение метода ToString для вывода информации об изделии
        public override string ToString()
        {
            return $"Название: {Name} Язык программирования: {Programming_language} Тип: {Prod_type} Версия: {Version}";
        }

        // Виртуальный(может быть переопределен в наследниках) метод для вывода информации об одной компаненте
        public virtual void Print_One_component()
        {
            Console.WriteLine(this?.ToString()); // Безопасно: если this = null, вернет null
        }
        // Метод языка програмирования, теперь уже именно компаненты
        abstract public void Database(); // Делаем метод абст-ным, тем самым передаем его на реализацию наследникам и формально удовлетворяем интерфейс I_izdelie

        // Метод изменения данных компонента. Доступ protected !!!!(в наследниках будет переопределяться)
        protected virtual void Change_Component(string name, string prog_lang, ProductType prod, string vers)
        {
            Name = name;
            Programming_language = prog_lang;
            Prod_type = prod;
            Version = vers;
        }

        // --------------------------- Абстрактные свойства

        // Абстрактное свойство для количества строк кода (будет реализовано в наследниках)
        public abstract int Code_lines { get; set; } 
       
        
        // Вспомогательный статический метод для вывода разделительной линии
        public static void Print_Line()
        {
            Console.WriteLine("---------------------------------------------------");
        }


    }
}
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lab_3_cherepnin
{
    [Serializable]
    public class Order_Manager : Component  //класс менеджер заявок
    {
        // Реализация наследуемых элементов ----------------------------------------
        // Метод базы данных, теперь уже именно менеджера заявок
        public override void Database()
        {
            Console.WriteLine("Используемая БД PSQL ");
        }

        // Приватное поле для хранения количества строк кода
        private int code_lines;// Поле для свойства Code_lines,закрытое

        // Реализуем абстрактное свойство // override Обязательно !!!!!! иначе new если скрываем свойство родителя, но тут реализация абст-го свойства так что скрыть в любом случае не получится
        // Количество строк в коде  Реализация абстрактного свойства Code_lines из базового класса
        public override int Code_lines
        {
            get => code_lines;
            set
            {
                if (value > 30 && value < 1000) code_lines = value;
                else code_lines = 250;
            }
        }

        // Переопределение метода ToString()
        // Создает строку, описывающюю объект данного класса
        public override string ToString()
        {
            string str = $" Количество строк кода :{Code_lines}";
            return base.ToString() + str; // Создаем новый ToString() на основании старого
        }

        // Работает с полем moved . Переопределение свойства типа продукта с ограничением только для фронтенд-компонентов
        public override ProductType Prod_type
        {
            get => prod_type;
            set
            {
                if (value == ProductType.frontend_component) prod_type = value;

                else prod_type = ProductType.unknown_type;
            }
        }

        // Конструкторы класса Order_Manager
        // По умолчанию
        public Order_Manager()
        {
            this.Code_lines = 330;
            this.Name = "Order Manager";
            this.Prod_type = ProductType.frontend_component;
        }

        // С параметрами, с передачей параметров в базовый конструктор  класса Components
        public Order_Manager(string name, string prog_lang, ProductType prod, string vers, int code_lines= 330) : base(name, prog_lang, ProductType.frontend_component, vers)
        {
            Code_lines = code_lines;
        }

       

    }
}
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lab_3_cherepnin
{
    public class Srv_Restrictions : Component //класс серверная компанента  для проверки ограничений
    {
        // Реализация наследуемых элементов ----------------------------------------
        // Реализация абстрактного метода Database из интерфейса I_izdelie
        public override void Database()
        {
            Console.WriteLine("Используемая БД PSQL ");
        }
        // Приватное поле для хранения количества строк кода
        private int code_lines;// Поле для свойства Code_lines,закрытое

        // Реализуем абстрактное свойство // override Обязательно !!!!!! иначе new если скрываем свойство родителя, но тут реализация абст-го свойства так что скрыть в любом случае не получится
        // Количество строк в коде, Реализация абстрактного свойства Code_lines из базового класса
        public override int Code_lines
        {
            get => code_lines;
            set
            {
                if (value > 50 && value < 1500) code_lines = value;
                else code_lines = 400;
            }
        }

        // Переопределение метода ToString()
        // Создает строку, описывающюю объект данного класса
        public override string ToString()
        {
            string str = $" Количество строк кода :{Code_lines}";
            return base.ToString() + str; // Создаем новый ToString() на основании старого
        }

        // Работает с полем moved .Переопределение свойства типа продукта с ограничением только для серверных компонентов
        public override ProductType Prod_type
        {
            get => prod_type;
            set
            {
                if (value == ProductType.server_component) prod_type = value;

                else prod_type = ProductType.unknown_type;
            }
        }

        // Конструкторы класса Order_Manager
        // По умолчанию
        public Srv_Restrictions()
        {
            this.Code_lines = 330;
            this.Name = "srvRestrictions";
            this.Prod_type = ProductType.server_component;
        }

        // С параметрами, с передачей параметров в базовый конструктор  класса Components
        public Srv_Restrictions(string name, string prog_lang, ProductType prod, string vers, int code_lines = 500) : base(name, prog_lang, ProductType.server_component, vers)
        {
            Code_lines = code_lines;
        }
    }
}
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Xml.Serialization;

namespace lab_3_cherepnin
{
    [Serializable]
    public class Collection_components
    {
        // Создать коллекцию на основе динамического массива.
        List<Component> arr_components = new List<Component>();

        // Метод заполнения коллекции arr_components
        public void Filling_Collection()
        {
            arr_components.Add(new Order_Manager());
            arr_components.Add(new Srv_Restrictions());
            arr_components.Add(new Order_Manager("Order manage Sber", "C#", ProductType.frontend_component, "1.1.1", 700));
            arr_components.Add(new Srv_Restrictions("srv Restrictions Tbank", "C#", ProductType.server_component, "1.1.0", 800));   
        }


        

        //Это метод для вывода технической информации (TTX) о коллекции, Count - сколько элементов находится в коллекции , Capacity - сколько элементов может вместить коллекция

        public void Print_arr_components_TTX()
        {
            Console.Write("Всего компонентов: "); Component.Print_count_component(); Console.WriteLine();
            Console.WriteLine($" Кол-во объектов в массиве arr_components :{arr_components.Count}");
            Console.WriteLine($" Кол-во ячеек в массиве arr_components :{arr_components.Capacity}");
            Component.Print_Line();
        }

        // Метод вывода всех объектов на экран
        public void Print_arr_components()
        {
            Console.Write("Всего компонентов: "); Component.Print_count_component(); Console.WriteLine();
            foreach (var item in arr_components)
            {
                item.Print_One_component();
            }
            Component.Print_Line();
        }

        // Индексатор для доступа к элементам коллекции по индексу
        public Component this[int Index]
        {
            get
            {
                if (Index >= 0 && Index < arr_components.Count) return arr_components[Index];
                else return null;
            }
        }

        //	 Метод вывода одного объекта из коллекции по индексу с обработкой исключений
        // Печать одной компаненты из коллекции по заданному индексу
        public void Print_One_Item_from_Collection(int Index)
        {
            try
            {
                arr_components[Index].Print_One_component();
                Component.Print_Line();
            }
            catch
            {
                Console.WriteLine(" ВНИМАНИЕ!\n " +
                    "В методе  Print_One_Item_from_Collection класса Collection_components\n " +
                    "Применён не корректный индекс к коллекции arr_components");
                Component.Print_Line();
            }
        }

        // Метод добавления объектов в коллекцию "по умолчанию" (без параметров)
        public void Add_components() // Добавление пустого объекта в массив
        {
            Console.WriteLine(" Метод добавления компанент в коллекцию \"по умолчанию\"");
            Console.WriteLine(" Какую компаненту Вы хотите добавить ?");
            Console.Write(" Если серверную, нажмите 1, если фронтовую, нажмите 2 :");

            int assa = Regex_Metod(); // Получение выбора пользователя

            Add_srv(assa);
            Add_front(assa);
            
        }

        // Вспомогательный метод для валидации ввода (1 или 2)
        public int Regex_Metod()
        {
            string str = Console.ReadLine();

            // Паттерн регулярного выражения для проверки ввода
            string pattern = @"^[1|2]$";

            Match match = Regex.Match(str, pattern);

            Console.WriteLine(match.ToString());

            //  Console.ReadKey();- для чтения одного нажатия клавиши с консоли.

            try
            {
                return Convert.ToInt32(match.ToString());
            }
            catch
            {
                Console.WriteLine(" Получено неверное управляющее значение");
                return 0;
            }
        }

        //Метод добавления серверного компонента по умолчанию
        public void Add_srv(int assa)
        {
            if (assa == 1)
            {
                Console.WriteLine(" Вы решили добавить серверную компаненту");
                arr_components.Add(new Srv_Restrictions());

                
            }
        }

        //Метод добавления фронтового компонента по умолчанию
        public void Add_front(int assa)
        {
            if (assa == 2)
            {
                Console.WriteLine(" Вы решили добавить фронтовую компаненту");
                arr_components.Add(new Order_Manager());
            }
        }

        // Метод добавления компонентов с параметрами, вводимыми пользователем
        public void Add_component_with_Parameters() // Добавление объекта в массив c параметрами
        {
            Console.WriteLine(" Метод добавления компонент в коллекцию ");
            Console.WriteLine(" Какую компаненту Вы хотите добавить ?");
            Console.Write(" Если серверную, нажмите 1, если фронтовую, нажмите 2 :");

            int assa = Regex_Metod();

            Add_srv_with_Parameters(assa);
            Add_front_with_Parameters(assa);
        }

        // Метод добавления серверного компонента с параметрами
        public void Add_srv_with_Parameters(int assa)
        {
            if (assa != 1) return;

            Console.WriteLine(" Вы решили добавить серверную компаненту");

            Console.Write(" Введите имя :");
            string name = Console.ReadLine();

            Console.Write(" Введите язык программирования :");
            string progLang = Console.ReadLine();

            Console.Write(" Введите версию :");
            string version = Console.ReadLine();

            Console.Write(" Введите количество строк кода (целое число) :");
            int codeLines;
            try
            {
                codeLines = Int32.Parse(Console.ReadLine());
                if (codeLines < 50 || codeLines > 1500)
                {
                    Console.WriteLine(" Количество строк кода должно быть от 50 до 1500");
                    Console.WriteLine(" Будет установлено 400 строк");
                    codeLines = 400;
                }
            }
            catch
            {
                Console.WriteLine(" Неправильные данные для количества строк кода");
                Console.WriteLine(" Будет установлено 400 строк");
                codeLines = 400;
            }

            // Создаем серверный компонент с параметрами
            arr_components.Add(new Srv_Restrictions(name, progLang, ProductType.server_component, version, codeLines));
            Console.WriteLine(" Серверная компонента успешно добавлена!");
        }

        // Метод добавления фронтового компонента с параметрами
        public void Add_front_with_Parameters(int assa)
        {
            if (assa != 2) return;

            Console.WriteLine(" Вы решили добавить фронтовую компаненту");

            Console.Write(" Введите имя :");
            string name = Console.ReadLine();

            Console.Write(" Введите язык программирования :");
            string progLang = Console.ReadLine();

            Console.Write(" Введите версию :");
            string version = Console.ReadLine();

            Console.Write(" Введите количество строк кода (целое число) :");
            int codeLines;
            try
            {
                codeLines = Int32.Parse(Console.ReadLine());
                if (codeLines < 30 || codeLines > 1000)
                {
                    Console.WriteLine(" Количество строк кода должно быть от 30 до 1000");
                    Console.WriteLine(" Будет установлено 250 строк");
                    codeLines = 250;
                }
            }
            catch
            {
                Console.WriteLine(" Неправильные данные для количества строк кода");
                Console.WriteLine(" Будет установлено 250 строк");
                codeLines = 250;
            }

            // Создаем фронтовой компонент с параметрами
            arr_components.Add(new Order_Manager(name, progLang, ProductType.frontend_component, version, codeLines));
            Console.WriteLine(" Фронтовая компонента успешно добавлена!");
        }

        // Метод удаления объекта из коллекции по индексу
        public void Del_comp(int index)
        {
            try
            {
                arr_components.RemoveAt(index);
                Component.Decrement_component(); 
            }
            catch
            {
                Console.WriteLine(" Удалить элемент из коллекции arr_components не удалось");
                Console.WriteLine(" Проверьте правильность индекса удаления");
            }
        }

        // Метод изменения объекта в коллекции (замена по индексу)
        public void Change_Item(int index, Component comp)
        {
            arr_components.RemoveAt(index); // Удаляем старый элемент
            Component.Decrement_component();
            arr_components.Insert(index, comp);// Вставляем новый элемент взамен старого
        }
        

        // Метод полной очистки коллекции arr_components
        public void Clearing_Collection()
        {
            // Уменьшаем счетчик только на компоненты в этой коллекции
            for (int i = 0; i < arr_components.Count; i++)
            {
                Component.Decrement_component();
            }

            // Теперь очищаем коллекцию
            arr_components.Clear();
        }

        // Метод поиска объекта в коллекции по имени
        // по полю Name 
        public int Find_compone_name(string str)
        {
            int Index = 0;
            foreach (var item in arr_components)
            {
                if (item.Name == str) return Index;
                Index++;
            }
            return -1;
        }
        //	сериализация и десериализация коллекции объектов в файл.
        // ------------------------------------------------------------------------------------------------
        public void Serialize_Collection_Component()
        {
            string xmlFilePath = "save_arr_components.xml"; //записываем имя файла
                                                            //   Serialize_Component serialize_Component = new Serialize_Component();

            // Проводим сериализацию коллекции в файл в формате XML
            SerializeToXml(arr_components, xmlFilePath);
        }

        public void DeSerialize_Collection_Component()
        {
            string xmlFilePath = "save_arr_components.xml";
            //  Serialize_Bird serialize_Bird = new Serialize_Bird();

            // Проводим сериализацию коллекции в файл в формате XML
            arr_components = DeserializeFromXml(xmlFilePath);
        }

        // метод сериализациии
        public static void SerializeToXml(List<Component> components, string filePath)
        {
            XmlSerializer serializer = new XmlSerializer(typeof(List<Component>));

            using (FileStream fs = new FileStream(filePath, FileMode.OpenOrCreate))
            {
                serializer.Serialize(fs, components);
            }
        }
        // метод десереализации
        public static List<Component> DeserializeFromXml(string filePath)
        {
            XmlSerializer serializer = new XmlSerializer(typeof(List<Component>));

            using (FileStream fs = new FileStream(filePath, FileMode.Open))
            {
                return (List<Component>)serializer.Deserialize(fs);
            }
        }
        
    }
}
```
