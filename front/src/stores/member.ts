import { defineStore } from 'pinia';
import axios from 'axios';
import { ElMessage, ElMessageBox } from 'element-plus';

export interface Member {
  name: string;
  phone: string;
  email: string;
  address: string;
  register_date: string;
  member_type: string;
  expiry_date: string;
  member_id: string;
}

export const useMemberStore = defineStore('member', {
    state: () => ({
        members: [] as Member[],
    }),
    actions: {
        async fetchMembers() {
            const response = await axios.get('http://127.0.0.1:8000/member');
            this.members = response.data;
        },
        async deleteMembers(id: string) {
            try {
                await ElMessageBox.confirm('确定要删除该会员吗？', '提示', {
                    confirmButtonText: '确认',
                    cancelButtonText: '取消',
                    type: 'warning',
                });
                await axios.delete(`http://127.0.0.1:8000/member/${id}`);
                ElMessage.success('删除成功');
                await this.fetchMembers();
            } catch (error: any) {
                if (error === 'cancel' || error === 'close') {
                    ElMessage.info('已取消删除');
                } else {
                    console.error('删除失败:', error);
                    ElMessage.error('删除失败，请稍后重试');
                }
            }
        },
        async addMembers(data: any) {
            await axios.post('http://127.0.0.1:8000/member', data);
        }
    }
})