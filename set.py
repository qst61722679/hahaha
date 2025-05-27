class GenderSelectorNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "gender_choice": (["Female", "Male"], {
                    "default": "Female"
                }),  # 下拉选择框，选择性别
            }
        }

    RETURN_TYPES = ("INT",)  # 输出整数类型，1 代表 Female，2 代表 Male
    RETURN_NAMES = ("gender_value",)  # 输出端口名称
    FUNCTION = "select_gender"  # 执行函数名称
    CATEGORY = "Custom Nodes"  # 节点分类

    def select_gender(self, gender_choice):
        # 根据用户选择返回对应的整数值
        return (1 if gender_choice == "Female" else 2,)

# 注册节点
NODE_CLASS_MAPPINGS = {
    "GenderSelectorNode": GenderSelectorNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GenderSelectorNode": "Gender Selector (Int)"
}
