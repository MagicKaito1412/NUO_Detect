import {
    Alert,
    Autocomplete,
    Avatar,
    Badge,
    Button,
    ButtonGroup,
    Card,
    Carousel,
    CarouselItem,
    Checkbox,
    CheckboxButton,
    CheckboxGroup,
    Collapse,
    CollapseItem,
    DatePicker,
    Dialog,
    Divider,
    Dropdown,
    DropdownItem,
    DropdownMenu,
    Form,
    Icon,
    Image,
    Input,
    InputNumber,
    Link,
    Loading,
    Menu,
    MenuItem,
    MenuItemGroup,
    Message,
    MessageBox,
    Notification,
    Option,
    OptionGroup,
    PageHeader,
    Pagination,
    Popover,
    Progress,
    Radio,
    RadioButton,
    RadioGroup,
    Rate,
    Select,
    Slider,
    Submenu,
    Switch,
    Table,
    TableColumn,
    TabPane,
    Tabs,
    Tag,
    TimePicker,
    TimeSelect,
    Tooltip,
    Tree,
    Upload
} from 'element-ui';
import lang from 'element-ui/lib/locale/lang/ru-RU'
import locale from 'element-ui/lib/locale'

export default {
    install(Vue) {

        // element ui
        locale.use(lang);
        Vue.use(Pagination);
        Vue.use(Dialog);
        Vue.use(Autocomplete);
        Vue.use(Dropdown);
        Vue.use(DropdownMenu);
        Vue.use(DropdownItem);
        Vue.use(Menu);
        Vue.use(Submenu);
        Vue.use(MenuItem);
        Vue.use(MenuItemGroup);
        Vue.use(Input);
        Vue.use(InputNumber);
        Vue.use(Radio);
        Vue.use(RadioGroup);
        Vue.use(RadioButton);
        Vue.use(Checkbox);
        Vue.use(CheckboxButton);
        Vue.use(CheckboxGroup);
        Vue.use(Switch);
        Vue.use(Select);
        Vue.use(Option);
        Vue.use(OptionGroup);
        Vue.use(Button);
        Vue.use(ButtonGroup);
        Vue.use(Table);
        Vue.use(TableColumn);
        Vue.use(DatePicker);
        Vue.use(TimeSelect);
        Vue.use(TimePicker);
        Vue.use(Popover);
        Vue.use(Tooltip);
        Vue.use(Tabs);
        Vue.use(TabPane);
        Vue.use(Tag);
        Vue.use(Tree);
        Vue.use(Alert);
        Vue.use(Slider);
        Vue.use(Icon);
        Vue.use(Upload);
        Vue.use(Progress);
        Vue.use(Badge);
        Vue.use(Card);
        Vue.use(Rate);
        Vue.use(Carousel);
        Vue.use(CarouselItem);
        Vue.use(Collapse);
        Vue.use(CollapseItem);
        Vue.use(Link);
        Vue.use(Divider);
        Vue.use(Image);
        Vue.use(PageHeader);
        Vue.use(Avatar);
        Vue.use(Form);

        Vue.use(Loading.directive);

        Vue.prototype.$loading = Loading.service;
        Vue.prototype.$msgbox = MessageBox;
        Vue.prototype.$alert = MessageBox.alert;
        Vue.prototype.$confirm = MessageBox.confirm;
        Vue.prototype.$prompt = MessageBox.prompt;
        Vue.prototype.$notify = Notification;
        Vue.prototype.$message = Message;
    }
}
