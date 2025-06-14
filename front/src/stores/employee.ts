import { defineStore } from 'pinia';
import axios from 'axios';
import { ElMessage, ElMessageBox } from 'element-plus';

export interface Employee {
  name: string;
  position: string;
  phone: string;
  email: string;
  hire_date: string;
  salary: number;
  manager_id: string;
  employee_id: string;
}

export const useEmployeeStore = defineStore('employee', {
    state: () => ({
        employee: [] as Employee[],
    }),
    actions: {
        async fetchEmployee() {
            const response = await axios.get('http://127.0.0.1:8000/employee');
            this.employee = response.data;
        },
        async deleteEmployee(id: string) {
            try {
                await ElMessageBox.confirm('确定要删除该员工吗？', '提示', {
                    confirmButtonText: '确认',
                    cancelButtonText: '取消',
                    type: 'warning',
                });
                await axios.delete(`http://127.0.0.1:8000/employee/${id}`);
                ElMessage.success('删除成功');
                await this.fetchEmployee();
            } catch (error: any) {
                if (error === 'cancel' || error === 'close') {
                    ElMessage.info('已取消删除');
                } else {
                    console.error('删除失败:', error);
                    ElMessage.error('删除失败，请稍后重试');
                }
            }
        },
        async addEmployee(data: any) {
            await axios.post('http://127.0.0.1:8000/employee', data);
        }
    }
})