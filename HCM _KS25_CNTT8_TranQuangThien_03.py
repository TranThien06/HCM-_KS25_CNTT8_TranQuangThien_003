class CourseRegistration:
    def __init__(self, id, student_name, course_name, tuition_fee, discount, extra_fee):
        
        self.id = id
        self.student_name = student_name
        self.course_name = course_name
        self.tuition_fee = tuition_fee
        self.discount = discount
        self.extra_fee = extra_fee
        
        self.total_fee = 0
        self.fee_type = ""
        
        self.calculate_total_fee()
        self.classify_fee()
    
    def calculate_total_fee(self):
        self.total_fee = float(self.tuition_fee - self.discount + self.extra_fee)
        
    def classify_fee(self):
        if self.total_fee >= 15000000:
            self.fee_type="Rất cao"
        elif self.total_fee >= 7000000:
            self.fee_type="Cao"
        elif self.total_fee >= 3000000:
            self.fee_type = "Trung bình"
        else:
            self.fee_type="Yếu"
            
    # slecalculate_total_fee()
    # classify_fee()


class CourseRegistrationManager:
    def __init__(self):
        self.registrations = []
        
        
    # hàm chỗ trợ check tiền
    def check_money(self, prompt):
        while True:
            try:
                money = float(input(prompt))
                if money >= 0:
                    return money
                print("Số tiền phải lớn hơn hoặc bằng 0")
            except ValueError:
                print("Vui lòng nhập đúng định dạng")
        
    # chúc năng 1
    def show_all(self):
        print("Hiển thị danh sách")
        print(f"{"Mã ĐK":<10} | {"Họ tên":<20} | {"Tên khóa học":<20} | {"Học phí gốc":<15} | {"Giảm giá":<15} | {"Phụ phí":<15} | {"Tổng học phí":<15} | {"Phân loại":<15}")
        print("=" * 145)
        for r in self.registrations:
            print(f"{r.id:<10} | {r.student_name:<20} | {r.course_name:<20} | {r.tuition_fee:<15} | {r.discount:<15} | {r.extra_fee:<15} | {r.total_fee:<15} | {r.fee_type:<15}")
    
    # chức năng 2
    def add_registration(self):
        while True:
            id = input("Nhập vào mã đăng ký: ").strip().upper()
            if not id:
                print("ID không được rỗng")
                continue
            is_id = False
            for r in self.registrations:
                if r.id == id:
                    is_id = True
                    break
            if is_id:
                print("ID đã tồn tại")
                continue
            break
        while True:
            stu_name = input("Nhập vào tên học viên: ").strip().title()
            if not stu_name:
                print("Tên học viên không được để trống")
                continue
            break
        while True:
            cour_name = input("Nhập vào tên khóa học: ").strip().title()
            if not cour_name:
                print("Tên khóa không được rỗng")
                continue
            break
        tuition = self.check_money("Nhập học phí gốc: ")
        # discount = self.check_money("Nhập số tiền giảm giá: ")
        while True:
            discount = float(input("Nhập vào giảm giá: "))
            try:
                if discount < 0:
                    print("Số tiền phải lớn hơn 0")
                    continue
                elif discount > tuition:
                    print("Số tiền giảm giá không được lớn hơn học phí gốc")
                    continue
                else:
                    break
            except ValueError:
                print("Vui lòng nhập đúng định dạng")
                continue
            break
        extra = self.check_money("Nhập phụ phí: ")
        
        
        new_regis = CourseRegistration(id, stu_name, cour_name, tuition, discount, extra)
        
        manager.registrations.append(new_regis)
        print("Thêm khóa học thành công")
        
    # chức năng 3: 
    def update_registration(self):
        id_update = input("Nhập vào id muốn cập nhật: ").strip().upper()
        
        for r in self.registrations:
            if r.id == id_update:
                
                
                r.tuition_fee = self.check_money("Nhập vào học phí cập nhật: ")
                r.discount = self.check_money("Nhập vào giảm giá cập nhật: ")
                r.extra_fee = self.check_money("Nhập vào phụ phí cập nhật: ")
                # tuition = self.check_money("Nhập vào học phí cập nhật: ")
                # discount = self.check_money("Nhập vào giảm giá cập nhật: ")
                # extra = self.check_money("Nhập vào phụ phí cập nhật: ")
                
                r.calculate_total_fee()
                r.classify_fee()
                
                print("Cập nhật thành công")
                return
        print("Không tìm thấy ID")
        
    # chức năng 4:
    def delete_registration(self):
        id_delete = input("Nhập vào mã muốn xóa: ").strip().upper()
        
        for r in self.registrations:
            if r.id == id_delete:
                confirm = input("Bạn có chắc chắc muốn xóa khóa học này không (Y/N): ").strip().upper()
                if confirm == "Y":
                    self.registrations.remove(r)
                    print("Xóa khóa học thành công")
                    return
                elif confirm == "N":
                    print("Yêu cầu xóa được hủy")
                    return
                else:
                    print("Lựa chọn không hợp lệ")
                    return
        print("Không tìm thấy khóa học")
    # 
        # --- Chức năng 5. Tìm kiếm theo tên gần đúng ---
    # def search_registration(self):
    #     keyword = input("Nhập tên học viên cần tìm: ").strip().lower()

    #     if not keyword:
    #         print(" Lỗi: Từ khóa tìm kiếm không được để trống!")
    #         return

    #     results = [r for r in self.registrations if keyword in r.student_name.lower()]
    #     if results:
    #         print(f"\n Kết quả tìm kiếm cho tên học viên '{keyword}':")
    #         print(results)
    #     else:
    #         print(" Không tìm thấy khóa học phù hợp.")
                
manager = CourseRegistrationManager()
manager.registrations.append(CourseRegistration("JU01", "Trần Quang Thiện", "Python", 6000000, 2000000, 1000000))    
manager.registrations.append(CourseRegistration("JU02", "Trần Quang B", "Fastapi", 15000000, 1000000, 3000000))   
manager.registrations.append(CourseRegistration("JU03", "Trần  B", "Fastapi", 15000000, 1000000, 3000000))   
while True:
    choice = input('''
================ Menu ================
1. Hiển thị danh sách đăng ký khóa học
2. Thêm đăng ký khóa học mới
3. Cập nhập học phí
4. Xóa đăng ký khóa học
5. Tìm kiếm đăng ký
6. Thoát
=======================================
Nhập lựa chọn của bạn: ''')
    
    match choice:
        case "1":
            manager.show_all()
        case "2":
            manager.add_registration()
        case "3":
            manager.update_registration()
        case "4":
            manager.delete_registration()
        case "5":
            pass
        case "6":
            print("Chương trình đã được thoát")
            break
        case _:
            print("Lựa chọn không hợp lệ")
        