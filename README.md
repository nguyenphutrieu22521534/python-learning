# python-learning
Repository này là nơi lưu trữ các ghi chú, ví dụ và tài liệu học tập về Python. "Hẹ hẹ hẹ"

## Danh sách câu hỏi lý thuyết
- Phân biệt các loại class trong Python
- Phân biệt các loại  method trong Python
- Phân biệt Methods và Dunder
- Phân biệt giữa module và package

### Phân biệt các loại class trong Python
- Regular Class: Lớp cơ bản nhất, dùng để tạo các đối tượng với thuộc tính và phương thức riêng.
- Abstract Class: 	Là một lớp không thể tạo instance (đối tượng) trực tiếp. Nó được dùng như một lớp cơ sở để các lớp khác kế thừa. Nó định nghĩa các phương thức mà các lớp con bắt buộc phải triển khai. Sử dụng module abc.
- Dataclass: Class được trang bị sẵn các method như `__init__`, `__repr__`, `__eq__` để làm việc với dữ liệu. Sử dụng decorator `@dataclass`.

### Phân biệt các loại  method trong Python
- Get/Set Method: Method cung cấp quyền truy cập được kiểm soát vào các thuộc tính của đối tượng.
- Class Method: Method nhận tham số `cls` (class itself), được khai báo với `@classmethod`. Dùng để tạo factory method hoặc thao tác với class-level attributes.
- Static Method: Method không nhận tham số `self` hay `cls`, được khai báo với `@staticmethod`. Dùng cho các utility function không phụ thuộc vào instance hay class.
- Override Method: Method Overriding là việc class con định nghĩa lại method đã có trong class cha với implementation mới.

### Phân biệt Methods và Dunder
- Methods: Là các phương thức được định nghĩa bên trong một class. Chúng được phân loại dựa trên cách chúng được gọi và mục đích.
- Dunder: Là các phương thức đặc biệt có tên được bao quanh bởi double underscores

### Phân biệt giữa module và package
- Module: Đơn giản là một file Python (có đuôi .py). Nó có thể chứa các hàm, class, và biến. Ta có thể import một module để sử dụng code của nó trong một file khác.
- Package: Là một thư mục chứa nhiều module (và các package con khác). Để Python nhận diện một thư mục là một package, nó bắt buộc phải có file __init__.py (có thể để trống). Packages giúp tổ chức code ở cấp độ cao hơn, tránh xung đột tên.
