import unittest
from Segregate import Segregation


class Testing(unittest.TestCase):
    def setUp(self):
        self.seg = Segregation()
        self.t = []
        self.t_result = []
        self.s = ""
        self.reset_data()

    def instantiate_data(self):
        self.t = [
                ['x', 'x', 'o', 'o', 'x', 'o', 'x', 'o', 'x', 'o'],
                ['x', 'o', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x'],
                ['o', 'x', 'x', ' ', 'x', 'o', 'o', 'x', 'o', 'x'],
                ['o', 'x', 'x', 'x', 'o', 'o', 'x', ' ', 'x', 'o'],
                ['x', 'o', 'o', 'x', 'o', 'x', 'o', 'x', 'x', 'o'],
                ['x', 'o', 'x', ' ', 'x', 'x', 'o', ' ', 'o', 'x'],
                ['x', 'x', 'o', 'o', 'x', 'o', 'x', 'o', 'x', 'o'],
                ['x', 'o', ' ', 'o', 'x', 'o', 'o', 'x', 'o', 'o'],
                ['o', 'x', 'x', 'x', 'o', 'o', ' ', 'o', 'x', 'o'],
                ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'x', 'o', 'x']
            ]

    def reset_data(self):
        self.seg.clear_data()

    def reset_sub_tables(self):
        self.self.clear_sub_tables()

    def test_load_table_list_pass(self):
        self.instantiate_data()
        self.seg.load_data(self.t)
        self.assertEqual(self.seg.table, self.t)

    def test_load_table_list_fail(self):
        self.t = [
            ['x', 'x', 'o', 'o', 'x', 'o', 'x', 'o', 'x', 'o'],
            ['x', 'o', 'o', 'x', 'o', 'x', 'o', 'x'],
            ['o', 'x', 'x', ' ', 'x', 'o', 'o', 'x', 'o', 'x']
        ]
        self.seg.load_data(self.t)
        self.assertEqual(self.seg.table, [])

    def test_load_table_list_empty(self):
        self.seg.load_data(self.t)
        self.assertEqual(self.seg.table, [])

    def test_load_table_string_pass(self):
        self.s = "xxooxoxoxoxooxoxoxoxoxx xooxoxoxxxoox xoxooxoxoxxoxox xxo oxxxooxoxoxoxo oxooxoooxxxoo oxooooooooxox"
        self.instantiate_data()
        self.seg.load_data(self.s, 10)
        self.assertEqual(self.seg.table, self.t)

    def test_load_table_string_fail(self):
        self.s = "xxooxoxoxoxxoxoxxoxox xxo oxxxooxoxoxoxo oxooxoooxxxoo oxooooooooxox"
        self.seg.load_data(self.s, 10)
        self.assertEqual(self.seg.table, self.t)

    def test_load_table_string_empty(self):
        self.seg.load_data(self.t)
        self.assertEqual(self.seg.table, [])

    def test_set_sub_table_pass(self):
        self.instantiate_data()
        self.seg.load_data(self.t)
        self.sub_t = [
            ['x', 'x', 'o'],
            ['x', 'o', 'o'],
            ['o', 'x', 'x']
        ]

        point1 = (0, 0)
        point2 = (2, 2)
        self.seg.add_sub_table(point1, point2)
        self.assertEqual(self.seg.sub_tables, [self.sub_t])

    def test_set_multiple_sub_table_pass(self):
        self.instantiate_data()
        self.seg.load_data(self.t)
        sub_ts = []

        sub_t = [
            ['x', 'x', 'o'],
            ['x', 'o', 'o'],
            ['o', 'x', 'x']
        ]
        sub_ts.append(sub_t)

        point1 = (0, 0)
        point2 = (2, 2)
        self.seg.add_sub_table(point1, point2)

        sub_t = [
            ['x', 'o', 'o'],
            ['x', 'o', 'x'],
            [' ', 'x', 'x']
        ]
        sub_ts.append(sub_t)

        point1 = (3, 3)
        point2 = (5, 5)
        self.seg.add_sub_table(point1, point2)
        self.assertEqual(self.seg.sub_tables, sub_ts)

        self.reset_data()
        self.assertEqual(self.seg.sub_tables, [])
        self.assertEqual(self.seg.table, [])

    @unittest.SkipTest
    def test_DISABLE_set_sub_table_fail_same_axis(self):
        self.instantiate_data()
        self.seg.load_data(self.t)

        point1 = (0, 0)
        point2 = (0, 3)
        self.seg.add_sub_table(point1, point2)
        self.assertEqual(self.seg.sub_tables, [])

    def test_set_sub_table_fail_no_loaded_data(self):
        point1 = (0, 0)
        point2 = (2, 2)
        self.seg.add_sub_table(point1, point2)
        self.assertEqual(self.seg.sub_tables, [])

    def test_index_of_dissimilarity_pass(self):
        block1 = ['x', 'x']
        block2 = ['o', 'o']
        block3 = ['x', 'o']
        block4 = ['o', 'x']
        temp = [block1, block2, block3, block4]
        self.seg.sub_tables.append(temp)
        self.assertEqual(self.seg.get_index_of_dissimilarity(), 0.5)

    def test_index_of_dissimilarity_fail_empty_tables(self):
        self.seg.clear_data()
        self.assertEqual(self.seg.get_index_of_dissimilarity(), None)

    def test_index_of_dissimilarity_fail_only_one_group(self):
        block1 = ['x', 'x']
        self.seg.sub_tables.append(block1)
        self.seg.sub_tables.append(block1)

        self.assertEqual(self.seg.get_index_of_dissimilarity(), None)

    def test_get_adjacent_node_pass(self):
        self.t = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(self.seg.get_adjacent_XY(self.t, 1, 1), [1, 4, 7, 2, 8, 3, 6, 9])
        self.assertEqual(self.seg.get_adjacent_XY(self.t, 0, 0), [4, 2, 5])
        self.assertEqual(self.seg.get_adjacent_XY(self.t, 0, 2), [4, 5, 8])
        self.assertEqual(self.seg.get_adjacent_XY(self.t, 2, 0), [2, 5, 6])

    def test_is_happy_pass(self):
        self.instantiate_data()
        self.seg.load_data(self.t)
        self.t = [
            ['x', ' ', 'o'],
            ['x', ' ', 'o'],
            ['x', ' ', 'o']
        ]

        self.assertTrue(self.seg.is_happy(self.t, 0, 0))
        self.assertTrue(self.seg.is_happy(self.t, 0, 1))
        self.assertTrue(self.seg.is_happy(self.t, 0, 2))
        self.assertTrue(self.seg.is_happy(self.t, 2, 0))
        self.assertTrue(self.seg.is_happy(self.t, 2, 1))
        self.assertTrue(self.seg.is_happy(self.t, 2, 2))

    # more than 1 possible outcome, 50% chance to pass
    @unittest.SkipTest
    def test_run_schelling_model_pass(self):
        self.t = [
            ['x', ' ', 'o'],
            ['x', 'o', 'o'],
            ['x', ' ', ' ']
        ]

        self.seg.load_data(self.t)

        point1 = (0, 0)
        point2 = (2, 2)
        self.seg.add_sub_table(point1, point2)

        self.t_result = [[
            ['x', ' ', 'o'],
            ['x', ' ', 'o'],
            ['x', ' ', 'o']
        ]]

        self.assertEqual(self.seg.run_schelling_model(50), self.t_result)


if __name__ == '__main__':
    unittest.main()
