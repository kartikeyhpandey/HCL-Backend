
from django.core.management.base import BaseCommand
from api.models import ProductResult, DeviceResult

class Command(BaseCommand):
    help = 'Load product results data into the database'

    def handle(self, *args, **options):
        data = [
            {
                "product": 1,
                "status": "Active",
                "connectivity_speed": "High",
                "devices": [
                {
                    "device": 1,
                    "status": "Connected",
                    "connectivity_speed": "Medium"
                },
                {
                    "device": 2,
                    "status": "Disconnected",
                    "connectivity_speed": "Low"
                }
                ]
            },
            {
                "product": 2,
                "status": "Inactive",
                "connectivity_speed": "Low",
                "devices": [
                {
                    "device": 1,
                    "status": "Connected",
                    "connectivity_speed": "High"
                }
                ]
            }
        ]

        for item in data:
            product_result = ProductResult.objects.create(
                product_id=item['product'],
                status=item['status'],
                connectivity_speed=item['connectivity_speed']
            )

            devices_data = item.get('devices', [])
            for device_data in devices_data:
                DeviceResult.objects.create(
                    device_id=device_data['device'],
                    product_result=product_result,
                    status=device_data['status'],
                    connectivity_speed=device_data['connectivity_speed']
                )

        self.stdout.write(self.style.SUCCESS('Successfully loaded product results data'))
