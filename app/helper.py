import streamlit as st

class DataHelper():

    def get_personal_data(self):
        return {
            "title": "Thông tin cá nhân",
            "fields": [
                {"key": "gioiTinh", "value": "male", "input_type": "text",
                        "label": "Giới tính (chip nfc)", "is_required": True},
                {"key": "ngaySinh", "value": "yyyy-mm-dd", "input_type": "text",
                        "label": "Ngày sinh khách hàng", "is_required": True},
                {"key": "title_code", "value": 0, "input_type": "int", "min": 0, "max":9999999999,
                        "label": "Mã chức vụ của khách.", "is_required": True, "help":" Vd: Chủ doanh nghiệp - 00001"},
                {"key": "nam_cu_tru", "value": 0, "input_type": "number",
                        "label": "Số năm cư trú", "is_required": True},
                {"key": "application_create_time", "value": "yyyy-mm-dd", "input_type": "text",
                        "label": "application_create_time", "is_required": True},
                {"key": "cccd", "value": "123456789", "input_type": "text",
                 "label": "CCCD", "is_required": False},
                {"key": "ngayCap", "value": "yyyy-mm-dd", "input_type": "text",
                        "label": "Ngày cấp cccd/cmnd/hộ chiếu", "is_required": True},
                {
                    "key": "effective_date",
                    "value": "yyyy-mm-dd",
                    "input_type": "text",
                    "label": "Ngày có hiệu lực",
                    "is_required": False
                },
                {
                    "key": "expiration_date",
                    "value": "yyyy-mm-dd",
                    "input_type": "text",
                    "label": "Ngày hết hạn",
                    "is_required": False
                },
                {"key": "X_PER_ADD_PROVINCE_CODE", "value": 0, "input_type": "number",
                        "label": "X_PER_ADD_PROVINCE_CODE", "is_required": True},
                {"key": "X_PER_ADD_DISTRICT_CODE", "value": 0, "input_type": "number",
                        "label": "X_PER_ADD_DISTRICT_CODE", "is_required": True}
            ]
        }

    def get_address_data(self):
        return {
            "title": "Thông tin địa chỉ",
            "fields": [
                {"key": "temporary_address_provinces_code", "value": 0,
                    "input_type": "number", "label": "Mã tỉnh tạm trú", "is_required": True},
                {"key": "temporary_address_district_code", "value": 0,
                    "input_type": "number", "label": "Mã huyện tạm trú", "is_required": True},

                {"key": "addressProvincesCode", "value": 0, "input_type": "number",
                    "label": "Nơi ở hiện tại: mã tỉnh", "is_required": True},
                {"key": "addressDistrictCode", "value": 0, "input_type": "number",
                    "label": "Nơi ở hiện tại: mã quận/huyện", "is_required": True}, {
                    "key": "homeTownProvincesCode",
                    "value": 0,
                    "input_type": "number",
                    "label": "Mã tỉnh nơi ở hiện tại",
                    "is_required": False
                },
                {
                    "key": "homeTownDistrictCode",
                    "value": 0,
                    "input_type": "number",
                    "label": "Mã huyện nơi ở hiện tại",
                    "is_required": False
                },
                {
                    "key": "homeTownWardsCode",
                    "value": 0,
                    "input_type": "number",
                    "label": "Mã xã phường nơi ở hiện tại",
                    "is_required": False
                },
                {
                    "key": "addressWardsCode",
                    "value": 0,
                    "input_type": "number",
                    "label": "Mã xã phường nơi ở",
                    "is_required": False
                },
                {
                    "key": "ward_code",
                    "value": 0,
                    "input_type": "number",
                    "label": "Mã xã phường",
                    "is_required": False
                },
                {
                    "key": "thang_cu_tru",
                    "value": 0,
                    "input_type": "number",
                    "label": "Tháng cư trú",
                    "is_required": False
                },
                {
                    "key": "ma_tt_noi_cu_tru",
                    "value": "P",
                    "input_type": "text",
                    "label": "Mã tình trạng nơi cư trú",
                    "is_required": False
                }
            ]
        }

    def get_additional_data(self):
        return {
            "title": "Thông tin thêm",
            "fields": [
                {
                    "key": "dtDiDong",
                           "value": "string",
                           "input_type": "text",
                           "label": "Số điện thoại di động",
                           "is_required": False
                },
                {"key": "tenChongHoacVo", "value": "string", "input_type": "text",
                 "label": "Tên chồng hoặc vợ", "is_required": False},
                {"key": "nghi_ngo_lua_dao", "value": 0, "input_type": "checkbox",
                 "label": "Nghi ngờ lừa đảo", "is_required": False},
                {"key": "y_kien_tham_dinh", "value": "Dong y", "input_type": "text",
                 "label": "Ý kiến thẩm định", "is_required": False},
                {"key": "work_from", "value": "yyyy-mm-dd", "input_type": "text",
                 "label": "Ngày bắt đầu làm việc", "is_required": True},
                {
                    "key": "ma_nghe_nghiep",
                    "value": 0,
                    "input_type": "number",
                    "label": "Mã nghề nghiệp",
                    "is_required": False
                },
                {
                    "key": "ma_trinh_do_hoc_van",
                    "value": "HV0",
                    "input_type": "text",
                    "label": "Mã trình độ học vấn",
                    "is_required": True
                },
                {"key": "work_to", "value": "yyyy-mm-dd", "input_type": "text",
                 "label": "Ngày kết thúc làm việc", "is_required": True},
                {"key": "check_cic", "value": 0, "input_type": "checkbox",
                 "label": "Đã check cic hay chưa", "is_required": True},
                {
                    "key": "highest_debt_group",
                    "value": 0,
                    "input_type": "checkbox",
                    "label": "Khách hàng đã rơi xuống nhóm nợ xấu hay chưa",
                    "is_required": False
                },
                {"key": "total_current_outstanding_balance", "value": 0, "input_type": "number",
                 "label": "Tổng các khoản tiền còn lại mà người dùng cần phải trả", "is_required": False}
            ]
        }

    def get_insurance_data(self):
        return {
            "title": "Thông tin bảo hiểm",
            "fields": [
                {"key": "so_tien_bao_hiem_y", "value": 0, "input_type": "number",
                    "label": "Số tiền bảo hiểm", "is_required": False},
                {"key": "phi_bao_hiem", "value": 0, "input_type": "number",
                    "label": "Phí bảo hiểm", "is_required": False},
                {"key": "ma_nha_cung_cap", "value": "AAA", "input_type": "text",
                    "label": "Mã của nhà cung cấp bảo hiểm", "is_required": False},
                {"key": "ma_chu_ky_bao_hiem", "value": "string", "input_type": "text",
                    "label": "Mã chu kỳ bảo hiểm", "is_required": False},
                {"key": "ty_le_so_tien_duoc_bao_hiem", "value": 100, "input_type": "int",
                    "label": "Tỷ lệ % số tiền được bảo hiểm.", "is_required": False, "min": 1, "max":500, "help": "Vd: 140, 180"},
                {"key": "ty_le_bao_hiem", "value": 0, "input_type": "number",
                    "label": "Tỷ lệ bảo hiểm", "is_required": False},
            ]

        }

    def get_financail_data(self):
        return {"title": "Thông tin tài chính", "fields":
                [
                    {"key": "is_nguoi_phu_thuoc", "value": 0, "input_type": "checkbox",
                        "label": "Có người phụ thuộc hay không", "is_required": True},
                    {
                        "key": "so_nguoi_phu_thuoc",
                        "value": 0,
                        "input_type": "int",
                        "label": "Số người phụ thuộc",
                        "is_required": True,
                        "min": 0,
                        "max":100
                    },
                    {"key": "is_no_vay_khac", "value": 0, "input_type": "checkbox",
                        "label": "Có nợ vay khác hay không", "is_required": True},
                    {"key": "is_thu_nhap_khac", "value": 0, "input_type": "checkbox",
                        "label": "Có nguồn thu nhập khác hay không", "is_required": True},
                    {"key": "thu_nhap_thang", "value": 0, "input_type": "number",
                        "label": "Thu nhập hàng tháng", "is_required": True},
                    {"key": "thu_nhap_khac", "value": 0, "input_type": "number",
                        "label": "Thu nhập khác", "is_required": True},
                    {"key": "suggested_monthly_payment", "value": 0, "input_type": "number",
                        "label": "Số tiền hằng tháng phải trả", "is_required": True},
                    {"key": "chi_phi_sinh_hoat_hang_thang", "value": 0, "input_type": "number",
                        "label": "Chi phí sinh hoạt hàng tháng", "is_required": True},
                    {"key": "diem_DTI", "value": 0, "input_type": "number",
                        "label": "Điểm DTI ban đầu của hồ sơ", "is_required": True},
                    {"key": "dti_reality", "value": 0, "input_type": "number",
                        "label": "DTI thực", "is_required": True},
                    {
                        "key": "income_adjusted_by_adecco",
                        "value": 0,
                        "input_type": "number",
                        "label": "Thu nhập đã điều chỉnh theo adecco",
                        "is_required": False
                    },
                    {
                        "key": "is_delay_payment",
                        "value": 0,
                        "input_type": "number",
                        "label": "Có trễ hạn thanh toán hay không",
                        "is_required": False
                    },
                ]

                }

    def get_dealer_data(self):
        return {
            "title": "Thông tin đại lý vay",
            "fields": [
                {"key": "system_code", "value": "string", "input_type": "text",
                    "label": "Mã hệ thống đại lý", "is_required": True},
                {"key": "status_y", "value": 1, "input_type": "checkbox",
                    "label": "Trạng thái active của dealer. 0 hoặc 1", "is_required": True},
                {"key": "group_owner", "value": "03.Dong Nai 1", "input_type": "text",
                    "label": "Tên tổ chức quản lý của đại lý.", "is_required": True},
                {"key": "dealer_code", "value": 0, "input_type": "int",
                    "label": "Dealer code", "is_required": True, "min":0, "max":99999999999},
                {"key": "bank_province", "value": "TPHCM", "input_type": "text",
                    "label": "Tỉnh thành ngân hàng của dealer.", "is_required": False, "help":"Vd. Hồ Chí Minh"},
                {"key": "bank_code", "value": "string", "input_type": "text",
                    "label": "Mã ngân hàng của dealer.", "is_required": False, "help": " Vd: BIDV"},
                {"key": "bank_branch_name", "value": "string", "input_type": "text",
                    "label": "Tên chi nhánh ngân hàng của dealer", "is_required": False},
                {"key": "province_code", "value": 0, "input_type": "number",
                    "label": "Mã tỉnh/thành phố của nhà phân phối", "is_required": True},
                {"key": "district_code", "value": 0, "input_type": "number",
                    "label": "Mã huyện/quận của nhà phân phối", "is_required": True}
            ]

        }

    def get_pl_data(self):
        return {
            "title":  "Thông tin sản phẩm vay tiêu dùng",
            "fields": [
                {"key": "so_tien_vay_goc", "value": 0, "input_type": "number",
                    "label": "Số tiền vay gốc của khách hàng", "is_required": True},
                {"key": "tong_khoan_vay", "value": 0, "input_type": "number",
                    "label": "Tổng giá trị khoản vay (gốc lẫn lãi)", "is_required": True},
                {"key": "ky_han_vay", "value": 0, "input_type": "number",
                    "label": "Kỳ hạn vay", "is_required": True},
                {"key": "ma_muc_dich_vay", "value": 0, "input_type": "int",
                    "label": "Mã mục đích vay", "is_required": True, "min": 0, "max":8},
                {"key": "lai_suat_giai_doan_1", "value": 0, "input_type": "number",
                    "label": "Lãi suất giai đoạn 1", "is_required": True},
                {"key": "ky_han_giai_doan_1", "value": 0, "input_type": "number",
                    "label": "Kỳ hạn giai đoạn 1", "is_required": False},
                {"key": "PL_specific_field_1", "input_type": "text", "value": "",
                    "label": "Trường riêng của Personal Loan 1", "is_required": True},
                {"key": "PL_specific_field_2", "input_type": "number", "value": 0,
                    "label": "Trường riêng của Personal Loan 2", "is_required": True}
            ]
        }

    def get_mb_data(self):
        return {
            "title": "Thông tin sản phẩm vay xe máy",
            "fields": [
                {"key": "gia_xe", "value": 0, "input_type": "number",
                    "label": "Giá xe", "is_required": True},
                {"key": "ty_le_tra_truoc", "value": 0, "input_type": "number",
                    "label": "Tỷ lệ trả trước", "is_required": True},
                {"key": "so_tien_tra_truoc", "value": 0, "input_type": "number",
                    "label": "Số tiền trả trước", "is_required": True},
                {"key": "so_tien_vay_goc", "value": 0, "input_type": "number",
                    "label": "Số tiền vay gốc của khách hàng", "is_required": True},
                {"key": "tong_khoan_vay", "value": 0, "input_type": "number",
                    "label": "Tổng giá trị khoản vay (gốc lẫn lãi)", "is_required": True},
                {"key": "nam_san_xuat", "value": 0, "input_type": "number",
                    "label": "Năm sản xuất", "is_required": False},

                {
                    "key": "mau_sac",
                    "value": "string",
                    "input_type": "text",
                    "label": "Màu sắc của xe",
                    "is_required": False
                },
                {
                    "key": "ma_nhan_hieu",
                    "value": 0,
                    "input_type": "number",
                    "label": "Mã nhãn hiệu xe",
                    "is_required": False
                },
                {"key": "ky_han_vay", "value": 0, "input_type": "number",
                    "label": "Kỳ hạn vay", "is_required": True},
                {"key": "ky_han_giai_doan_1", "value": 0, "input_type": "number",
                    "label": "Kỳ hạn giai đoạn 1", "is_required": True},
                {"key": "ma_muc_dich_vay", "value": 0, "input_type": "int",
                    "label": "Mã mục đích vay", "is_required": True, "min": 0, "max":8},
                {
                    "key": "promotion_code",
                    "value": "string",
                    "input_type": "text",
                    "label": "Mã khuyến mãi",
                    "is_required": False
                },
            ]
        }

    def get_nc_data(self):
        return {
            "title": "Thông tin sản phẩm vay cho xe Oto",
            "fields": [
                {"key": "gia_xe", "value": 0, "input_type": "number",
                    "label": "Giá xe", "is_required": True},
                {"key": "ty_le_tra_truoc", "value": 0, "input_type": "number",
                    "label": "Tỷ lệ trả trước", "is_required": True},
                {"key": "so_tien_tra_truoc", "value": 0, "input_type": "number",
                    "label": "Số tiền trả trước", "is_required": True},
                {"key": "so_tien_vay_goc", "value": 0, "input_type": "number",
                    "label": "Số tiền vay gốc của khách hàng", "is_required": True},
                {"key": "tong_khoan_vay", "value": 0, "input_type": "number",
                    "label": "Tổng giá trị khoản vay (gốc lẫn lãi)", "is_required": True},
                {"key": "ky_han_vay", "value": 0, "input_type": "number",
                    "label": "Kỳ hạn vay", "is_required": True},
                {"key": "ky_han_giai_doan_1", "value": 0, "input_type": "number",
                    "label": "Kỳ hạn giai đoạn 1", "is_required": True},
                {"key": "ma_muc_dich_vay", "value": 0, "input_type": "int",
                    "label": "Mã mục đích vay", "is_required": True, "min":0, "max":8},
                {"key": "nam_san_xuat", "value": 0, "input_type": "number",
                 "label": "Năm sản xuất", "is_required": True}
            ]
        }

    def get_truck_data(self):
        return {
            "title": "Thông tin sản phẩm vay xe Tải",
            "fields": [
                {"key": "gia_xe", "value": 0, "input_type": "number",
                    "label": "Giá xe", "is_required": True},
                {"key": "ty_le_tra_truoc", "value": 0, "input_type": "number",
                    "label": "Tỷ lệ trả trước", "is_required": True},
                {"key": "so_tien_tra_truoc", "value": 0, "input_type": "number",
                    "label": "Số tiền trả trước", "is_required": True},
                {"key": "so_tien_vay_goc", "value": 0, "input_type": "number",
                    "label": "Số tiền vay gốc của khách hàng", "is_required": True},
                {"key": "tong_khoan_vay", "value": 0, "input_type": "number",
                    "label": "Tổng giá trị khoản vay (gốc lẫn lãi)", "is_required": True},
                {"key": "ky_han_vay", "value": 0, "input_type": "number",
                    "label": "Kỳ hạn vay", "is_required": True},
                {"key": "ky_han_giai_doan_1", "value": 0, "input_type": "number",
                    "label": "Kỳ hạn giai đoạn 1", "is_required": True},
                {"key": "ma_muc_dich_vay", "value": 0, "input_type": "int",
                    "label": "Mã mục đích vay", "is_required": True, "min":0, "max":8},
                {"key": "lai_suat_giai_doan_1", "value": 0, "input_type": "number",
                    "label": "Lãi suất giai đoạn 1", "is_required": True},
                {"key": "lai_suat_giai_doan_2", "value": 0, "input_type": "number",
                    "label": "Lãi suất giai đoạn 2", "is_required": False},
            ]
        }

    def get_input_data(self, loan_type: str):
        if loan_type == 'Personal Loan':
            return {
                "required": {
                    "so_tien_vay_goc": st.session_state.get('so_tien_vay_goc', 0),
                    "tong_khoan_vay": st.session_state.get('tong_khoan_vay', 0),
                    "is_nguoi_phu_thuoc": int(st.session_state.get('is_nguoi_phu_thuoc', False)),
                    "is_no_vay_khac": int(st.session_state.get('is_no_vay_khac', False)),
                    "is_thu_nhap_khac": int(st.session_state.get('is_thu_nhap_khac', False)),
                    "suggested_monthly_payment": st.session_state.get('suggested_monthly_payment', 0),
                    "chi_phi_sinh_hoat_hang_thang": st.session_state.get('chi_phi_sinh_hoat_hang_thang', 0),
                    "diem_DTI": st.session_state.get('diem_DTI', 0),
                    "ky_han_vay": st.session_state.get('ky_han_vay', 0),
                    "ma_muc_dich_vay": st.session_state.get('ma_muc_dich_vay', 0),
                    "check_cic": int(st.session_state.get('check_cic', False)),
                    "thu_nhap_thang": st.session_state.get('thu_nhap_thang', 0),
                    "thu_nhap_khac": st.session_state.get('thu_nhap_khac', 0),
                    "dti_reality": st.session_state.get('dti_reality', 0),
                    "so_nguoi_phu_thuoc": st.session_state.get('so_nguoi_phu_thuoc', 0),
                    "system_code": st.session_state.get('system_code', "string"),
                    "status_y": int(st.session_state.get('status_y', False)),
                    "group_owner": st.session_state.get('group_owner', "03.Dong Nai 1"),
                    "lai_suat_giai_doan_1": st.session_state.get('lai_suat_giai_doan_1', 0),
                    "nam_cu_tru": st.session_state.get('nam_cu_tru', 0),
                    "gioiTinh": st.session_state.get('gioiTinh', "male"),
                    "title_code": st.session_state.get('title_code', 0),
                    "temporary_address_district_code": st.session_state.get('temporary_address_district_code', 0),
                    "temporary_address_provinces_code": st.session_state.get('temporary_address_provinces_code', 0),
                    "district_code": st.session_state.get('district_code', 0),
                    "province_code": st.session_state.get('province_code', 0),
                    "addressProvincesCode": st.session_state.get('addressProvincesCode', 0),
                    "addressDistrictCode": st.session_state.get('addressDistrictCode', 0),
                    "dealer_code": st.session_state.get('dealer_code', 0),
                    "ma_trinh_do_hoc_van": st.session_state.get('ma_trinh_do_hoc_van', "HV0"),
                    "application_create_time": st.session_state.get('application_create_time', "yyyy-mm-dd"),
                    "ngaySinh": st.session_state.get('ngaySinh', "yyyy-mm-dd"),
                    "ngayCap": st.session_state.get('ngayCap', "yyyy-mm-dd"),
                    "X_PER_ADD_PROVINCE_CODE": st.session_state.get('X_PER_ADD_PROVINCE_CODE', 0),
                    "X_PER_ADD_DISTRICT_CODE": st.session_state.get('X_PER_ADD_DISTRICT_CODE', 0),
                    "work_from": st.session_state.get('work_from', "yyyy-mm-dd"),
                    "work_to": st.session_state.get('work_to', "yyyy-mm-dd")
                },
                "optional": {
                    "so_tien_bao_hiem_y": st.session_state.get('so_tien_bao_hiem_y', 0),
                    "ky_han_giai_doan_1": st.session_state.get('ky_han_giai_doan_1', 0),
                    "total_current_outstanding_balance": st.session_state.get('total_current_outstanding_balance', 0),
                    "highest_debt_group": int(st.session_state.get('highest_debt_group', False)),
                    "bank_province": st.session_state.get('bank_province', "TPHCM"),
                    "is_required": st.session_state.get('is_required', "BHBB"),
                    "ma_nha_cung_cap": st.session_state.get('ma_nha_cung_cap', "AAA"),
                    "ty_le_so_tien_duoc_bao_hiem": st.session_state.get('ty_le_so_tien_duoc_bao_hiem', 100),
                    "ma_nghe_nghiep": st.session_state.get('ma_nghe_nghiep', 0),
                    "X_HaveCIC": st.session_state.get('X_HaveCIC', 0),
                    "phi_bao_hiem": st.session_state.get('phi_bao_hiem', 0),
                    "ma_chu_ky_bao_hiem": st.session_state.get('ma_chu_ky_bao_hiem', "string"),
                    "bank_branch_name": st.session_state.get('bank_branch_name', "string"),
                    "bank_code": st.session_state.get('bank_code', "string"),
                    "dtDiDong": st.session_state.get('dtDiDong', "string"),
                    "tenChongHoacVo": st.session_state.get('tenChongHoacVo', "string")
                }
            }
        elif loan_type == 'Motobike':
            return {
                "required": {
                    "gia_xe": st.session_state.get('gia_xe', 0),
                    "ty_le_tra_truoc": st.session_state.get('ty_le_tra_truoc', 0),
                    "so_tien_tra_truoc": st.session_state.get('so_tien_tra_truoc', 0),
                    "so_tien_vay_goc": st.session_state.get('so_tien_vay_goc', 0),
                    "tong_khoan_vay": st.session_state.get('tong_khoan_vay', 0),
                    "is_nguoi_phu_thuoc": int(st.session_state.get('is_nguoi_phu_thuoc', False)),
                    "is_no_vay_khac": int(st.session_state.get('is_no_vay_khac', False)),
                    "is_thu_nhap_khac": int(st.session_state.get('is_thu_nhap_khac', False)),
                    "suggested_monthly_payment": st.session_state.get('suggested_monthly_payment', 0),
                    "chi_phi_sinh_hoat_hang_thang": st.session_state.get('chi_phi_sinh_hoat_hang_thang', 0),
                    "diem_DTI": st.session_state.get('diem_DTI', 0),
                    "ky_han_vay": st.session_state.get('ky_han_vay', 0),
                    "ky_han_giai_doan_1": st.session_state.get('ky_han_giai_doan_1', 0),
                    "ma_muc_dich_vay": st.session_state.get('ma_muc_dich_vay', 0),
                    "check_cic": int(st.session_state.get('check_cic', False)),
                    "thu_nhap_thang": st.session_state.get('thu_nhap_thang', 0),
                    "thu_nhap_khac": st.session_state.get('thu_nhap_khac', 0),
                    "dti_reality": st.session_state.get('dti_reality', 0),
                    "group_owner": st.session_state.get('group_owner', "string"),
                    "nam_cu_tru": st.session_state.get('nam_cu_tru', 0),
                    "gioiTinh": st.session_state.get('gioiTinh', "male"),
                    "title_code": st.session_state.get('title_code', 0),
                    "temporary_address_provinces_code": st.session_state.get('temporary_address_provinces_code', 0),
                    "temporary_address_district_code": st.session_state.get('temporary_address_district_code', 0),
                    "province_code": st.session_state.get('province_code', 0),
                    "district_code": st.session_state.get('district_code', 0),
                    "addressProvincesCode": st.session_state.get('addressProvincesCode', 0),
                    "addressDistrictCode": st.session_state.get('addressDistrictCode', 0),
                    "dealer_code": st.session_state.get('dealer_code', 0),
                    "ma_trinh_do_hoc_van": st.session_state.get('ma_trinh_do_hoc_van', "HV0"),
                    "application_create_time": st.session_state.get('application_create_time', "yyyy-mm-dd"),
                    "ngaySinh": st.session_state.get('ngaySinh', "yyyy-mm-dd"),
                    "ngayCap": st.session_state.get('ngayCap', "yyyy-mm-dd"),
                    "X_PER_ADD_PROVINCE_CODE": st.session_state.get('X_PER_ADD_PROVINCE_CODE', 0),
                    "X_PER_ADD_DISTRICT_CODE": st.session_state.get('X_PER_ADD_DISTRICT_CODE', 0),
                    "work_from": st.session_state.get('work_from', "yyyy-mm-dd"),
                    "work_to": st.session_state.get('work_to', "yyyy-mm-dd")
                },
                "optional": {
                    "nam_san_xuat": st.session_state.get('nam_san_xuat', 0),
                    "ty_le_bao_hiem": st.session_state.get('ty_le_bao_hiem', 0),
                    "so_tien_bao_hiem_y": st.session_state.get('so_tien_bao_hiem_y', 0),
                    "total_current_outstanding_balance": st.session_state.get('total_current_outstanding_balance', 0),
                    "so_nguoi_phu_thuoc": st.session_state.get('so_nguoi_phu_thuoc', 0),
                    "highest_debt_group": int(st.session_state.get('highest_debt_group', False)),
                    "system_code": st.session_state.get('system_code', "string"),
                    "status_y": int(st.session_state.get('status_y', False)),
                    "bank_province": st.session_state.get('bank_province', "string"),
                    "is_required": st.session_state.get('is_required', 0),
                    "ma_nha_cung_cap": st.session_state.get('ma_nha_cung_cap', "string"),
                    "ty_le_so_tien_duoc_bao_hiem": st.session_state.get('ty_le_so_tien_duoc_bao_hiem', 0),
                    "lai_suat_giai_doan_1": st.session_state.get('lai_suat_giai_doan_1', 0),
                    "ma_nghe_nghiep": st.session_state.get('ma_nghe_nghiep', 0),
                    "phi_bao_hiem": st.session_state.get('phi_bao_hiem', 0),
                    "ma_chu_ky_bao_hiem": st.session_state.get('ma_chu_ky_bao_hiem', "string"),
                    "bank_branch_name": st.session_state.get('bank_branch_name', "string"),
                    "mau_sac": st.session_state.get('mau_sac', "string"),
                    "ma_nhan_hieu": st.session_state.get('ma_nhan_hieu', 0),
                    "temporary_address_wards_code": st.session_state.get('temporary_address_wards_code', 0),
                    "nghi_ngo_lua_dao": int(st.session_state.get('nghi_ngo_lua_dao', False)),
                    "y_kien_tham_dinh": st.session_state.get('y_kien_tham_dinh', "Dong y"),
                    "thang_cu_tru": st.session_state.get('thang_cu_tru', 0),
                    "ma_tt_noi_cu_tru": st.session_state.get('ma_tt_noi_cu_tru', "P"),
                    "promotion_code": st.session_state.get('promotion_code', "string"),
                    "income_adjusted_by_adecco": st.session_state.get('income_adjusted_by_adecco', 0),
                    "is_delay_payment": st.session_state.get('is_delay_payment', 0),
                    "homeTownProvincesCode": st.session_state.get('homeTownProvincesCode', 0),
                    "homeTownDistrictCode": st.session_state.get('homeTownDistrictCode', 0),
                    "homeTownWardsCode": st.session_state.get('homeTownWardsCode', 0),
                    "addressWardsCode": st.session_state.get('addressWardsCode', 0),
                    "ward_code": st.session_state.get('ward_code', 0),
                    "X_HaveCIC": st.session_state.get('X_HaveCIC', 0),
                    "bank_code": st.session_state.get('bank_code', "string"),
                    "tenChongHoacVo": st.session_state.get('tenChongHoacVo', "string"),
                    "dtDiDong": st.session_state.get('dtDiDong', "string"),
                    "effective_date": st.session_state.get('effective_date', "yyyy-mm-dd"),
                    "expiration_date": st.session_state.get('expiration_date', "yyyy-mm-dd")
                }
            }
        elif loan_type == 'New Car':
            return {
                "required": {
                    "gia_xe": st.session_state.get('gia_xe', 0),
                    "ty_le_tra_truoc": st.session_state.get('ty_le_tra_truoc', 0),
                    "so_tien_tra_truoc": st.session_state.get('so_tien_tra_truoc', 0),
                    "so_tien_vay_goc": st.session_state.get('so_tien_vay_goc', 0),
                    "tong_khoan_vay": st.session_state.get('tong_khoan_vay', 0),
                    "is_nguoi_phu_thuoc": int(st.session_state.get('is_nguoi_phu_thuoc', False)),
                    "is_no_vay_khac": int(st.session_state.get('is_no_vay_khac', False)),
                    "is_thu_nhap_khac": int(st.session_state.get('is_thu_nhap_khac', False)),
                    "suggested_monthly_payment": st.session_state.get('suggested_monthly_payment', 0),
                    "chi_phi_sinh_hoat_hang_thang": st.session_state.get('chi_phi_sinh_hoat_hang_thang', 0),
                    "diem_DTI": st.session_state.get('diem_DTI', 0),
                    "ky_han_vay": st.session_state.get('ky_han_vay', 0),
                    "ky_han_giai_doan_1": st.session_state.get('ky_han_giai_doan_1', 0),
                    "ma_muc_dich_vay": st.session_state.get('ma_muc_dich_vay', 0),
                    "check_cic": int(st.session_state.get('check_cic', False)),
                    "thu_nhap_thang": st.session_state.get('thu_nhap_thang', 0),
                    "thu_nhap_khac": st.session_state.get('thu_nhap_khac', 0),
                    "dti_reality": st.session_state.get('dti_reality', 0),
                    "group_owner": st.session_state.get('group_owner', "string"),
                    "lai_suat_giai_doan_1": st.session_state.get('lai_suat_giai_doan_1', 0),
                    "nam_cu_tru": st.session_state.get('nam_cu_tru', 0),
                    "gioiTinh": st.session_state.get('gioiTinh', "male"),
                    "title_code": st.session_state.get('title_code', 0),
                    "temporary_address_district_code": st.session_state.get('temporary_address_district_code', 0),
                    "temporary_address_provinces_code": st.session_state.get('temporary_address_provinces_code', 0),
                    "district_code": st.session_state.get('district_code', 0),
                    "province_code": st.session_state.get('province_code', 0),
                    "addressProvincesCode": st.session_state.get('addressProvincesCode', 0),
                    "addressDistrictCode": st.session_state.get('addressDistrictCode', 0),
                    "dealer_code": st.session_state.get('dealer_code', 0),
                    "ma_trinh_do_hoc_van": st.session_state.get('ma_trinh_do_hoc_van', "HV0"),
                    "application_create_time": st.session_state.get('application_create_time', "yyyy-mm-dd"),
                    "ngaySinh": st.session_state.get('ngaySinh', "yyyy-mm-dd"),
                    "ngayCap": st.session_state.get('ngayCap', "yyyy-mm-dd"),
                    "X_PER_ADD_PROVINCE_CODE": st.session_state.get('X_PER_ADD_PROVINCE_CODE', 0),
                    "X_PER_ADD_DISTRICT_CODE": st.session_state.get('X_PER_ADD_DISTRICT_CODE', 0),
                    "work_from": st.session_state.get('work_from', "yyyy-mm-dd"),
                    "work_to": st.session_state.get('work_to', "yyyy-mm-dd"),
                    "nam_san_xuat": st.session_state.get('nam_san_xuat', 0)
                },
                "optional": {
                    "so_nguoi_phu_thuoc": st.session_state.get('so_nguoi_phu_thuoc', 0),
                    "highest_debt_group": int(st.session_state.get('highest_debt_group', False)),
                    "system_code": st.session_state.get('system_code', "string"),
                    "status_y": int(st.session_state.get('status_y', False)),
                    "bank_province": st.session_state.get('bank_province', "string"),
                    "ma_nghe_nghiep": st.session_state.get('ma_nghe_nghiep', 0),
                    "X_HaveCIC": int(st.session_state.get('X_HaveCIC', False)),
                    "phi_bao_hiem": st.session_state.get('phi_bao_hiem', 0),
                    "bank_branch_name": st.session_state.get('bank_branch_name', "string"),
                    "lai_suat_giai_doan_2": st.session_state.get('lai_suat_giai_doan_2', 0),
                    "bank_code": st.session_state.get('bank_code', "string"),
                    "tenChongHoacVo": st.session_state.get('tenChongHoacVo', "string"),
                    "dtDiDong": st.session_state.get('dtDiDong', "string")
                }
            }
        elif loan_type == 'Truck':
            return {
                "required": {
                    "gia_xe": st.session_state.get('gia_xe', 0),
                    "ty_le_tra_truoc": st.session_state.get('ty_le_tra_truoc', 0),
                    "so_tien_tra_truoc": st.session_state.get('so_tien_tra_truoc', 0),
                    "so_tien_vay_goc": st.session_state.get('so_tien_vay_goc', 0),
                    "tong_khoan_vay": st.session_state.get('tong_khoan_vay', 0),
                    "is_nguoi_phu_thuoc": int(st.session_state.get('is_nguoi_phu_thuoc', False)),
                    "is_no_vay_khac": int(st.session_state.get('is_no_vay_khac', False)),
                    "is_thu_nhap_khac": int(st.session_state.get('is_thu_nhap_khac', False)),
                    "suggested_monthly_payment": st.session_state.get('suggested_monthly_payment', 0),
                    "chi_phi_sinh_hoat_hang_thang": st.session_state.get('chi_phi_sinh_hoat_hang_thang', 0),
                    "diem_DTI": st.session_state.get('diem_DTI', 0),
                    "ky_han_vay": st.session_state.get('ky_han_vay', 0),
                    "ky_han_giai_doan_1": st.session_state.get('ky_han_giai_doan_1', 0),
                    "ma_muc_dich_vay": st.session_state.get('ma_muc_dich_vay', 0),
                    "check_cic": int(st.session_state.get('check_cic', False)),
                    "thu_nhap_thang": st.session_state.get('thu_nhap_thang', 0),
                    "dti_reality": st.session_state.get('dti_reality', 0),
                    "system_code": st.session_state.get('system_code', "string"),
                    "group_owner": st.session_state.get('group_owner', "03.Dong Nai 1"),
                    "lai_suat_giai_doan_1": st.session_state.get('lai_suat_giai_doan_1', 0),
                    "nam_cu_tru": st.session_state.get('nam_cu_tru', 0),
                    "gioiTinh": st.session_state.get('gioiTinh', "male"),
                    "title_code": st.session_state.get('title_code', 0),
                    "temporary_address_provinces_code": st.session_state.get('temporary_address_provinces_code', 0),
                    "temporary_address_district_code": st.session_state.get('temporary_address_district_code', 0),
                    "province_code": st.session_state.get('province_code', 0),
                    "district_code": st.session_state.get('district_code', 0),
                    "addressProvincesCode": st.session_state.get('addressProvincesCode', 0),
                    "addressDistrictCode": st.session_state.get('addressDistrictCode', 0),
                    "dealer_code": st.session_state.get('dealer_code', 0),
                    "ma_trinh_do_hoc_van": st.session_state.get('ma_trinh_do_hoc_van', "HV0"),
                    "application_create_time": st.session_state.get('application_create_time', "yyyy-mm-dd"),
                    "ngaySinh": st.session_state.get('ngaySinh', "yyyy-mm-dd"),
                    "ngayCap": st.session_state.get('ngayCap', "yyyy-mm-dd"),
                    "X_PER_ADD_PROVINCE_CODE": st.session_state.get('X_PER_ADD_PROVINCE_CODE', 0),
                    "X_PER_ADD_DISTRICT_CODE": st.session_state.get('X_PER_ADD_DISTRICT_CODE', 0),
                    "work_from": st.session_state.get('work_from', "yyyy-mm-dd"),
                    "work_to": st.session_state.get('work_to', "yyyy-mm-dd"),
                    "nam_san_xuat": st.session_state.get('nam_san_xuat', 0)
                },
                "optional": {
                    "so_nguoi_phu_thuoc": st.session_state.get('so_nguoi_phu_thuoc', 0),
                    "highest_debt_group": int(st.session_state.get('highest_debt_group', False)),
                    "system_code": st.session_state.get('system_code', "string"),
                    "bank_province": st.session_state.get('bank_province', "TPHCM"),
                    "ma_nghe_nghiep": st.session_state.get('ma_nghe_nghiep', 0),
                    "X_HaveCIC": st.session_state.get('X_HaveCIC', 0),
                    "phi_bao_hiem": st.session_state.get('phi_bao_hiem', 0),
                    "bank_branch_name": st.session_state.get('bank_branch_name', "string"),
                    "status_y": int(st.session_state.get('status_y', False)),
                    "ma_chu_ky_bao_hiem": st.session_state.get('ma_chu_ky_bao_hiem', "string"),
                    "lai_suat_giai_doan_2": st.session_state.get('lai_suat_giai_doan_2', 0),
                    "ty_le_so_tien_duoc_bao_hiem": str(st.session_state.get('ty_le_so_tien_duoc_bao_hiem', "100%")),
                    "ma_nha_cung_cap": st.session_state.get('ma_nha_cung_cap', "AAA"),
                    "is_required": st.session_state.get('is_required', "BHTN,BHBB"),
                    "ty_le_bao_hiem": st.session_state.get('ty_le_bao_hiem', 0),
                    "so_tien_bao_hiem_y": st.session_state.get('so_tien_bao_hiem_y', 0),
                    "bank_code": st.session_state.get('bank_code', "string"),
                    "tenChongHoacVo": st.session_state.get('tenChongHoacVo', "string"),
                    "dtDiDong": st.session_state.get('dtDiDong', "string")
                }
            }
        else:
            return ""
