import unittest
import unittest.mock as mock
import view_regist

# how to test
# cd test_double
# nose2 -v --with-coverage --coverage src


class ViewRegistryTest(unittest.TestCase):
    def test_no_view_provided(self):
        result = view_regist.get_subblueprints()
        self.assertEqual(result, [])

    @mock.patch("view_regist.dir", return_value=[])
    def test_one_view_no_subviews(self, mock_dir):
        views = [mock.MagicMock()]
        views[0].module = "first"
        # print(views[0].module)
        result = view_regist.get_subblueprints(views)

        mock_dir.assert_called_once()
        self.assertEqual(result, ["first"])

    def test_one_view_one_sub(self):
        first = mock.MagicMock()
        second = mock.MagicMock()
        first.module = mock.MagicMock()
        first.module.url_prefix = "/first"
        first.subviews = [second]
        second.module = mock.MagicMock()
        second.module.url_prefix = "/second"
        views = [first]
        result = view_regist.get_subblueprints(views)

        self.assertEqual(result, [first.module, second.module])
