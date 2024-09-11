class DataHelper():

    def get_personal_data(self):
        return {
        "title": "Input Personal Form",
        "fields": [
            {
                "key": "age",
                "name": "Nam Sinh",
                "input_type": "number",
                "min": 0,
                "max": 100,
                "default": 18
            },
            {
                "key": "nam_cu_tru",
                "name": "Nam Cu Tru",
                "input_type": "number",
                "min": 0,
                "max": 100,
                "default": 30.0
            },
            {
                "key": "gioiTinh",
                "name": "Gioi Tinh",
                "input_type": "text",
                "min": None,
                "max": None,
                "default": "male"
            },
            {
                "key": "so_nguoi_phu_thuoc",
                "name": "So Nguoi Phu Thuoc",
                "input_type": "number",
                "min": 0,
                "max": 10,
                "default": 0.0
            },
            {
                "key": "current_address_district_code",
                "name": "Current Address District Code",
                "input_type": "number",
                "min": 0,
                "max": 1000,
                "default": 75.0
            },
            {
                "key": "current_address_provinces_code",
                "name": "Current Address Provinces Code",
                "input_type": "number",
                "min": 0,
                "max": 1000,
                "default": 741.0
            },
            {
                "key": "district_code",
                "name": "District Code",
                "input_type": "number",
                "min": 0,
                "max": 1000,
                "default": 75.0
            },
            {
                "key": "province_code",
                "name": "Province Code",
                "input_type": "number",
                "min": 0,
                "max": 1000,
                "default": 75.0
            },
            {
                "key": "addressProvincesCode",
                "name": "Address Provinces Code",
                "input_type": "number",
                "min": 0,
                "max": 1000,
                "default": 741.0
            },
            {
                "key": "addressDistrictCode",
                "name": "Address District Code",
                "input_type": "text",
                "min": None,
                "max": None,
                "default": "NN26"
            },
            {
                "key": "current_address_wards_code",
                "name": "Current Address Wards Code",
                "input_type": "number",
                "min": 0,
                "max": 10000,
                "default": 3026.0
            },
            {
                "key": "homeTownProvincesCode",
                "name": "Home Town Provinces Code",
                "input_type": "number",
                "min": 0,
                "max": 1,
                "default": 0.6156565656565657
            },
            {
                "key": "homeTownDistrictCode",
                "name": "Home Town District Code",
                "input_type": "number",
                "min": 0,
                "max": 10,
                "default": 1.52375
            },
            {
                "key": "homeTownWardsCode",
                "name": "Home Town Wards Code",
                "input_type": "number",
                "min": 0,
                "max": 1,
                "default": 0.085309025
            },
            {
                "key": "addressWardsCode",
                "name": "Address Wards Code",
                "input_type": "number",
                "min": 0,
                "max": 1,
                "default": 0.0
            },
            {
                "key": "ward_code",
                "name": "Ward Code",
                "input_type": "number",
                "min": 0,
                "max": 100000000,
                "default": 40000000.0
            }
        ]
    }

    def get_additional_data(self):
        return {
            "title": "Input Additional Form",
            "fields": [
                {
                    "key": "is_nguoi_phu_thuoc",
                    "name": "Co Nguoi Phu Thuoc",
                    "input_type": "boolean",
                    "min": None,
                    "max": None,
                    "default": 0.0
                },
                {
                    "key": "is_no_vay_khac",
                    "name": "Co Vay No Khac",
                    "input_type": "boolean",
                    "min": None,
                    "max": None,
                    "default": False
                },
                {
                    "key": "is_thu_nhap_khac",
                    "name": "Is Thu Nhap Khac",
                    "input_type": "boolean",
                    "min": None,
                    "max": None,
                    "default": False
                },
                {
                    "key": "check_cic",
                    "name": "Check CIC",
                    "input_type": "boolean",
                    "min": None,
                    "max": None,
                    "default": 1
                },
                {
                    "key": "highest_debt_group",
                    "name": "Highest Debt Group",
                    "input_type": "text",
                    "min": None,
                    "max": None,
                    "default": ""
                },
                {
                    "key": "system_code",
                    "name": "System Code",
                    "input_type": "text",
                    "min": None,
                    "max": None,
                    "default": "MB00029"
                },
                {
                    "key": "status_y",
                    "name": "Status Y",
                    "input_type": "number",
                    "min": 0,
                    "max": 1,
                    "default": 0.0
                },
                {
                    "key": "group_owner",
                    "name": "Group Owner",
                    "input_type": "text",
                    "min": None,
                    "max": None,
                    "default": "03.Dong Nai 2"
                },
                {
                    "key": "bank_province",
                    "name": "Bank Province",
                    "input_type": "text",
                    "min": None,
                    "max": None,
                    "default": ""
                },
                {
                    "key": "is_required",
                    "name": "Is Required",
                    "input_type": "boolean",
                    "min": None,
                    "max": None,
                    "default": 1.0
                },
                {
                    "key": "ma_nha_cung_cap",
                    "name": "Ma Nha Cung Cap",
                    "input_type": "text",
                    "min": None,
                    "max": None,
                    "default": "GIC"
                },
                {
                    "key": "title_code",
                    "name": "Title Code",
                    "input_type": "number",
                    "min": 0,
                    "max": 10,
                    "default": 1.0
                },
                {
                    "key": "TARGET",
                    "name": "TARGET",
                    "input_type": "number",
                    "min": 0,
                    "max": 1000,
                    "default": 741.0
                },
                {
                    "key": "ma_nghe_nghiep",
                    "name": "Ma Nghe Nghiep",
                    "input_type": "number",
                    "min": 0,
                    "max": 100,
                    "default": 2
                },
                {
                    "key": "bank_branch_name",
                    "name": "Bank Branch Name",
                    "input_type": "text",
                    "min": None,
                    "max": None,
                    "default": "HV5"
                },
                {
                    "key": "dealer_code",
                    "name": "Dealer Code",
                    "input_type": "text",
                    "min": None,
                    "max": None,
                    "default": ""
                },
                {
                    "key": "ma_trinh_do_hoc_van",
                    "name": "Ma Trinh Do Hoc Van",
                    "input_type": "text",
                    "min": None,
                    "max": None,
                    "default": ""
                },

                {
                    "key": "nghi_ngo_lua_dao",
                    "name": "Nghi Ngo Lua Dao",
                    "input_type": "text",
                    "min": None,
                    "max": None,
                    "default": "HV5"
                },
                {
                    "key": "y_kien_tham_dinh",
                    "name": "Y Kien Tham Dinh",
                    "input_type": "text",
                    "min": None,
                    "max": None,
                    "default": ""
                },
                {
                    "key": "thang_cu_tru",
                    "name": "Thang Cu Tru",
                    "input_type": "text",
                    "min": None,
                    "max": None,
                    "default": ""
                },
                {
                    "key": "ma_tt_noi_cu_tru",
                    "name": "Ma TT Noi Cu Tru",
                    "input_type": "text",
                    "min": None,
                    "max": None,
                    "default": "MB00029"
                },
                {
                    "key": "promotion_code",
                    "name": "Promotion Code",
                    "input_type": "number",
                    "min": 0,
                    "max": 100,
                    "default": 0.0
                }
            ]
        }

    def get_insurance_data(self):
        return {
            "title": "Input Insurance Form",
            "fields": [
                {
                    "key": "ty_le_bao_hiem",
                    "name": "Ty Le Bao Hiem",
                    "input_type": "number",
                    "min": 0,
                    "max": 1,
                    "default": 0.25
                },
                {
                    "key": "so_tien_bao_hiem_y",
                    "name": "So Tien Bao Hiem Y",
                    "input_type": "number",
                    "min": 0,
                    "max": 1000000000,
                    "default": 57500000.0
                },
                {
                    "key": "ty_le_so_tien_duoc_bao_hiem",
                    "name": "Ty Le So Tien Duoc Bao Hiem",
                    "input_type": "number",
                    "min": 0,
                    "max": 1,
                    "default": 0.0
                },
                {
                    "key": "phi_bao_hiem",
                    "name": "Phi Bao Hiem",
                    "input_type": "text",
                    "min": None,
                    "max": None,
                    "default": "month"
                },
                {
                    "key": "ma_chu_ky_bao_hiem",
                    "name": "Ma Chu Ky Bao Hiem",
                    "input_type": "text",
                    "min": None,
                    "max": None,
                    "default": ""
                }
            ]
        }

    def get_financail_data(self):
        return {"title": "Input Financial Form", "fields": [
            {
                "key": "diem_DTI",
                "name": "Diem DTI",
                "input_type": "number",
                "min": 0,
                "max": 100,
                "default": 22.04
            },
            {
                "key": "dti_reality",
                "name": "DTI Reality",
                "input_type": "number",
                "min": 0,
                "max": 100,
                "default": 22.04
            },
            {
                "key": "thu_nhap_thang",
                "name": "Thu Nhap Thang",
                "input_type": "number",
                "min": 0,
                "max": 100000000,
                "default": 30000000.0
            },
            {
                "key": "thu_nhap_khac",
                "name": "Thu Nhap Khac",
                "input_type": "number",
                "min": 0,
                "max": 100000000,
                "default": 10000000.0
            },
            {
                "key": "total_current_outstanding_balance",
                "name": "Total Current Outstanding Balance",
                "input_type": "number",
                "min": 0,
                "max": 100000000,
                "default": 3200000.0
            },
            {
                "key": "chi_phi_sinh_hoat_hang_thang",
                "name": "Chi Phi Sinh Hoat Hang Thang",
                "input_type": "number",
                "min": 0,
                "max": 100000000,
                "default": 3200000.0
            },
            {
                "key": "income_adjusted_by_adecco",
                "name": "Income Adjusted By Adecco",
                "input_type": "number",
                "min": 0,
                "max": 100,
                "default": 17.86153340751462
            },
            {
                "key": "is_delay_payment",
                "name": "Is Delay Payment",
                "input_type": "number",
                "min": 0,
                "max": 100000000,
                "default": 38050000.0
            }
        ]
        }

    def get_product_data(self):
        return {"title": "Input Product Form", "fields": [
            {
                "key": "nam_san_xuat",
                "name": "Nam San Xuat",
                "input_type": "text",
                "min": None,
                "max": None,
                "default": ""
            },
            {
                "key": "gia_xe",
                "name": "Gia Xe",
                "input_type": "number",
                "min": 0,
                "max": 1000000000,
                "default": 99000000.0
            },
            {
                "key": "mau_sac",
                "name": "Mau Sac",
                "input_type": "text",
                "min": None,
                "max": None,
                "default": ""
            },
            {
                "key": "ma_nhan_hieu",
                "name": "Ma Nhan Hieu",
                "input_type": "text",
                "min": None,
                "max": None,
                "default": ""
            },
            {
                "key": "ty_le_tra_truoc",
                "name": "Ty Le Tra Truoc",
                "input_type": "number",
                "min": 0,
                "max": 100,
                "default": 41.9192
            },
            {
                "key": "so_tien_tra_truoc",
                "name": "So Tien Tra Truoc",
                "input_type": "number",
                "min": 0,
                "max": 1000000000,
                "default": 41500000.0
            },
            {
                "key": "so_tien_vay_goc",
                "name": "So Tien Vay Goc",
                "input_type": "number",
                "min": 0,
                "max": 1000000000,
                "default": 57500000.0
            },
            {
                "key": "tong_khoan_vay",
                "name": "Tong Khoan Vay",
                "input_type": "number",
                "min": 0,
                "max": 1000000000,
                "default": 60950000.0
            },
            {
                "key": "lai_suat_giai_doan_1",
                "name": "Lai Suat Giai Doan 1",
                "input_type": "number",
                "min": 0,
                "max": 100,
                "default": 29.76
            },
            {
                "key": "ky_han_vay",
                "name": "Ky Han Vay",
                "input_type": "number",
                "min": 0,
                "max": 100,
                "default": 24.0
            },
            {
                "key": "ky_han_giai_doan_1",
                "name": "Ky Han Giai Doan 1",
                "input_type": "number",
                "min": 0,
                "max": 100,
                "default": 24.0
            },
            {
                "key": "ma_muc_dich_vay",
                "name": "Ma Muc Dich Vay",
                "input_type": "number",
                "min": 0,
                "max": 10,
                "default": 1.0
            },
            {
                "key": "suggested_monthly_payment",
                "name": "Suggested Monthly Payment",
                "input_type": "number",
                "min": 0,
                "max": 100000000,
                "default": 3412361.0
            }
        ]
        }
