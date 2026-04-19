# from django.core.management.base import BaseCommand
# import helpers

# from typing import Any
# from django.conf import settings

# STATIC_VENDOR_DIR=getattr(settings,'STATIC_VENDOR_DIR')
# VENDOR_STATICFILES={
 
#  "flowbite.min.css":"https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.mincss",
 
#  "flowbite.min.js":"https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.minjs",
 
    
# }



# class Command(BaseCommand):
    
#     def handle(self, *args, **options):
#         self.stdout.write("downloading vendor static files")
        
#         completed_urls=[]
#         for name,url in VENDOR_STATICFILES.items():
#             out_path=STATIC_VENDOR_DIR / name
#             dl_success= helpers.download_to_local(url,out_path)
#             if dl_success:
#                 completed_urls.append(url)
#             else:
#                 self.stdout.write(
#                     self.style.ERROR(f'failed to download{url}')
#                 )    
#             if set(completed_urls) == set(VENDOR_STATICFILES.values()):
#                 self.stdout.write(
#                     self.style.SUCCESS('Successfully updated all vendor static files.')
#                 )
#             else:
#                 self.stdout.write(
#                     self.style.WARNING('Some files were not updated.')
#                 )    

from django.core.management.base import BaseCommand
from django.conf import settings
from pathlib import Path
import helpers

STATIC_VENDOR_DIR = getattr(settings, "STATIC_VENDOR_DIR", None)

VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",
    "flowbite.min.js.map": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js.map",

}


class Command(BaseCommand):
    help = "Download vendor static files (CSS/JS) from CDN"

    def handle(self, *args, **options):
        self.stdout.write("Downloading vendor static files...")

        if not STATIC_VENDOR_DIR:
            self.stdout.write(self.style.ERROR("STATIC_VENDOR_DIR is not set in settings."))
            return

        completed_urls = []

        for name, url in VENDOR_STATICFILES.items():
            out_path = Path(STATIC_VENDOR_DIR) / name

            try:
                dl_success = helpers.download_to_local(url, out_path)

                if dl_success:
                    completed_urls.append(url)
                    self.stdout.write(self.style.SUCCESS(f"Downloaded: {name}"))
                else:
                    self.stdout.write(self.style.ERROR(f"Failed to download: {url}"))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error downloading {url}: {e}"))

        # Final status check (AFTER loop)
        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(
                self.style.SUCCESS("Successfully updated all vendor static files.")
            )
        else:
            self.stdout.write(
                self.style.WARNING("Some files were not updated.")
            )