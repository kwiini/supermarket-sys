import { defineStore } from 'pinia';
import axios from 'axios';
import { ElMessage, ElMessageBox } from 'element-plus';

export interface Sale {
  member_id: string;
  sale_date: string;
  total_amount: number;
  discount_amount: number;
  payment_method: string;
  employee_id: string;
  sale_id: string;
}

export const useSaleStore = defineStore('sale', {
    state: () => ({
        sales: [] as Sale[],
    }),
    actions: {
        async fetchSales() {
            const response = await axios.get('http://127.0.0.1:8000/sale');
            this.sales = response.data;
        },
        async deleteSales(id: string) {
            try {
                await ElMessageBox.confirm('确定要删除该销售记录吗？', '提示', {
                    confirmButtonText: '确认',
                    cancelButtonText: '取消',
                    type: 'warning',
                });
                await axios.delete(`http://127.0.0.1:8000/sale/${id}`);
                ElMessage.success('删除成功');
                await this.fetchSales();
            } catch (error: any) {
                if (error === 'cancel' || error === 'close') {
                    ElMessage.info('已取消删除');
                } else {
                    console.error('删除失败:', error);
                    ElMessage.error('删除失败，请稍后重试');
                }
            }
        },
        async addSales(data: any) {
            await axios.post('http://127.0.0.1:8000/sale', data);
        }
    }
})