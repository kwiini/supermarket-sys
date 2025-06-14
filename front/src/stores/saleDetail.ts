import { defineStore } from 'pinia';
import axios from 'axios';
import { ElMessage, ElMessageBox } from 'element-plus';

export interface SaleDetail {
  sale_id: string;
  product_id: string;
  quantity: number;
  unit_price: number;
  subtotal: number;
  detail_id: string;
}

export const useSaleDetailStore = defineStore('saleDetail', {
    state: () => ({
        salesDetail: [] as SaleDetail[],
    }),
    actions: {
        async fetchSalesDetail() {
            const response = await axios.get('http://127.0.0.1:8000/sale_detail');
            this.salesDetail = response.data;
        },
        async deleteSalesDetail(id: string) {
            try {
                await ElMessageBox.confirm('确定要删除该销售明细吗？', '提示', {
                    confirmButtonText: '确认',
                    cancelButtonText: '取消',
                    type: 'warning',
                });
                await axios.delete(`http://127.0.0.1:8000/sale_detail/${id}`);
                ElMessage.success('删除成功');
                await this.fetchSalesDetail();
            } catch (error: any) {
                if (error === 'cancel' || error === 'close') {
                    ElMessage.info('已取消删除');
                } else {
                    console.error('删除失败:', error);
                    ElMessage.error('删除失败，请稍后重试');
                }
            }
        },
        async addSalesDetail(data: any) {
            await axios.post('http://127.0.0.1:8000/sale_detail', data);
        }
    }
})